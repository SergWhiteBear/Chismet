import numpy as np
from matplotlib import pyplot as plt


def f(x, y):
    return (x ** 2) / (y ** 2)


#  Точное решение
def analytic(x):
    return np.cbrt(x ** 3 - 8)


#  Производная по x
def f_x(x, y):
    return (2 * x) / y ** 2


#  Производная по y
def f_y(x, y):
    return -2 * x ** 2 / y ** 3


#  Метод Эйлера
def get_Euler(x, y0, h, n, f):
    y = [0] * (n + 1)
    y[0] = y0
    for i in range(n):
        y[i + 1] = y[i] + f(x[i], y[i]) * h

    return y


#  Метод Тейлора второго порядка
def get_second_Teylor(x, y0, h, n, f):
    y = [0] * (n + 1)
    y[0] = y0
    for i in range(n):
        y[i + 1] = y[i] + f(x[i], y[i]) * h + h ** 2 / 2 * (f_x(x[i], y[i]) + f_y(x[i], y[i]) * f(x[i], y[i]))

    return y


#  Метод Адамса двухшаговый явный
def get_twostep_Adams(x, y0, h, n, f):
    y = [0] * (n + 1)
    y[0] = y0

    y[1] = y[0] + f(x[0], y[0]) * h + h ** 2 / 2 * (f_x(x[0], y[0]) + f_y(x[0], y[0]) * f(x[0], y[0]))

    for i in range(1, n):
        y[i + 1] = y[i] + (h / 2) * (3 * f(x[i], y[i]) - f(x[i - 1], y[i - 1]))

    return y


# Функция для расчета Средней Абсолютной ошибки
def calculate_mae(y_actual, y_calculated):
    return np.mean(np.abs(y_actual - y_calculated))


if __name__ == "__main__":
    arr_N = [10, 20, 30]
    results = {}
    for N in arr_N:
        h = 1 / N

        x = np.linspace(0.0, 1.0, num=N + 1)
        res_analytic = analytic(x)
        y_Euler = get_Euler(x, -2, h, N, f)
        y_Teylor = get_second_Teylor(x, -2, h, N, f)
        y_Adams = get_twostep_Adams(x, -2, h, N, f)
        results[N] = {
            'Точное решение': res_analytic,
            'Эйлер': y_Euler,
            'Тейлор': y_Teylor,
            'Адамс': y_Adams,
            'x': x
        }
        errors_Euler = calculate_mae(res_analytic, y_Euler)
        errors_Teylor = calculate_mae(res_analytic, y_Teylor)
        errors_Adams = calculate_mae(res_analytic, y_Adams)
        print(f'Средняя Абсолютная ошибки для разбиения {N}')
        print(f'Метод Эйлер явный = {errors_Euler}')
        print(f'Метод Тейлор второго порядка = {errors_Teylor}')
        print(f'Метод Адамс двухшаговый = {errors_Adams} \n')
        plt.figure(figsize=(18, 11))
        plt.plot(results[N]['x'], results[N]['Эйлер'], label=f'Эйлер N={N}')
        plt.plot(results[N]['x'], results[N]['Тейлор'], label=f'Тейлор N={N}')
        plt.plot(results[N]['x'], results[N]['Адамс'], label=f'Адамс N={N}')
        plt.plot(results[N]['x'], results[N]['Точное решение'], label=f'Точное решение N={N}',
                 linestyle='--')  # Точное решение для сравнения
        plt.title(f'Сравнение методов для N={N}')
        plt.xticks(np.linspace(0.0, 1.0, num=N + 1))
        plt.yticks(np.linspace(-2, -1.90, num=N + 1))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.savefig(f'diff_{N}.png')
        plt.show()
    names_methods = ['Точное решение', 'Эйлер', 'Тейлор', 'Адамс']
    for name in names_methods:
        plt.figure(figsize=(18, 11))
        plt.plot(results[10]['x'], results[10][name], label=f'{name} N=10')
        plt.plot(results[20]['x'], results[20][name], label=f'{name} N=20')
        plt.plot(results[30]['x'], results[30][name], label=f'{name} N=30')
        plt.title(f'Метод {name}')
        plt.xticks(np.linspace(0.0, 1.0, num=20 + 1))
        plt.yticks(np.linspace(-2, -1.90, num=20 + 1))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.savefig(f'{name}.png')
        plt.show()
