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


# Определение функции для вычисления средней абсолютной ошибки (MAE)
def mean_absolute_error(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))


# Определение функции для вычисления среднеквадратичной ошибки (MSE)
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


if __name__ == "__main__":
    arr_N = [10, 20, 30]

    for N in arr_N:
        h = 1 / N

        x = np.linspace(0.0, 1.0, num=N + 1)
        res_analytic = analytic(x)
        y_Euler = get_Euler(x, -2, h, N, f)
        y_Teylor = get_second_Teylor(x, -2, h, N, f)
        y_Adams = get_twostep_Adams(x, -2, h, N, f)
        print(mean_absolute_error(res_analytic, y_Euler))
        print(mean_absolute_error(res_analytic, y_Adams))
        print(mean_absolute_error(res_analytic, y_Teylor))


        plt.figure(figsize=(18, 11))
        plt.plot(x, y_Euler, label='Эйлер')
        #plt.plot(x, y_Teylor, label='Тейлор')
        #plt.plot(x, y_Adams, label='Адамс')
        #plt.plot(x, analytic(x), label='Точное реш.', linestyle='--')  # Точное решение для сравнения
        plt.title(f'Метод Эйлера для N={N}')
        plt.xticks(np.linspace(0.0, 1.0, num=N + 1))
        plt.yticks(np.linspace(-2, -1.90, num=N + 1))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.savefig(f' Euler_N_{N}.png')
        plt.show()
