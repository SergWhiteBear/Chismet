import math

# Погрешность
epsilon = 0.5 * 10 ** (-5)


# f`` - вторая производная
def f2(x: float):
    return 6 * math.sin(x ** 2) + 12 * x ** 2 * math.cos(x ** 2)


# f` первая производная
def f1(x: float):
    return 1 + 6 * x * math.sin(x ** 2)


# f функция
def f(x: float):
    return x - 3 * math.cos(x ** 2)


# Метод дихотомии
def dichotomy(a: float, b: float):
    n = 1
    while (abs(b - a) / 2) > epsilon:
        x_0 = (a + b) / 2
        if f(x_0) == 0:
            return x_0, n
        elif f(x_0) * f(b) < 0:
            a = x_0
        else:
            b = x_0
        n += 1
    return (a + b) / 2, n


# Метод Ньютона
def method_newton(x_curr: float):
    n = 0
    x_next = x_curr - f(x_curr) / f1(x_curr)
    while abs(x_next - x_curr) > epsilon:
        x_curr = x_next
        x_next = x_curr - f(x_curr) / f1(x_curr)
        n += 1

    return x_next, n


# Модифицированный метод Ньютона
def modified_method_newton(x_curr: float):
    n = 0
    x_0 = x_curr
    x_next = x_curr - f(x_curr) / f1(x_curr)
    while abs(x_next - x_curr) > epsilon:
        x_curr = x_next
        x_next = x_curr - f(x_curr) / f1(x_0)
        n += 1

    return x_next, n


# Метод хорд
def method_hord(a: float, b: float):
    f_x0 = f(b)
    n = 0
    while abs(f(a) / f1(a)) > epsilon:
        a = a - ((f(a) * (a - b)) / (f(a) - f_x0))
        n += 1

    return a, n


# Метод подвижных хорд
def method_movable_hord(a: float, b: float):
    n = 0
    c = b
    b = a - ((f(a) * (b - c)) / (f(a) - f(c)))
    while abs(f(a) / f1(a)) > epsilon:
        b = a - ((f(b) * (b - c)) / (f(a) - f(c)))
        c = a
        a = b
        n += 1
    return b, n


# Функция для метода простой итерации
def f_msi(x):
    return math.sqrt(math.acos(x / 3))


# Метод простой итерации
def method_simple_iteration(a: float, b: float):
    x = (a + b) / 2
    n = 0
    while abs(f(x) / f1(x)) > epsilon:
        x = abs(f_msi(x))
        n += 1

    return x, n


# Находил отрезки при помощи этой функции
def find_cut():
    a = 0
    b = 1
    while f(a) > 0 > f(b) or f(a) < 0 < f(b):
        b += 0.1
        if f(a) * f2(a) > 0 or f(b) * f2(b) > 0:
            print(a, b)


# Использовал для проверки номера в дихотомии
def check_num_iter_for_dichotomy(a: float, b: float, n):
    return n >= math.log((b - a) / epsilon, 2)


if __name__ == "__main__":
    a = 0
    b = 1.3
    x_n, n = dichotomy(a, b)
    print(f"x_n = {x_n}, n = {n}")
    x_n, n = method_newton(b)
    print(f"x_n = {x_n}, n = {n}")
    x_n, n = modified_method_newton(b)
    print(f"x_n = {x_n}, n = {n}")
    x_n, n = method_hord(a, b)
    print(f"x_n = {x_n}, n = {n}")
    x_n, n = method_movable_hord(a, b)
    print(f"x_n = {x_n}, n = {n}")
    x_n, n = method_simple_iteration(a, b)
    print(f"x_n = {x_n}, n = {n}")
    #print(check_num_iter_for_dichotomy(0, 1.3, 18))
