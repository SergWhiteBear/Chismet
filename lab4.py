import math
import numpy as np
from sympy import symbols, cos, diff, maximum, S, Interval


def f(x):
    return math.cos(x ** 4)


def get_trapezoid_method(h):
    x_i = np.arange(0.0, 1.0 + h, h)
    gen = (f(x_i[i]) + f(x_i[i + 1]) for i in range(len(x_i) - 1))
    return h / 2 * sum(gen)


def get_gregory_method(h):
    x_i = np.arange(0.0, 1.0 + h, h)
    m = int(1 / h)
    gen = (f(i) / 2 if (i == 0 or i == 1) else f(i) for i in x_i)
    res = h * (sum(gen)) + h / 24 * (
            -3 * f(x_i[0]) + 4 * f(x_i[1]) - f(x_i[2]) - 3 * f(x_i[m]) + 4 * f(x_i[m - 1]) - f(x_i[m - 2]))
    return res


steps = [0.1, 0.05, 0.025]
print('Формула трапеций:')
trapezoid_results = []
for h in steps:
    trapezoid_results.append(get_trapezoid_method(h))
    print(f'    h={h}   I[f]={get_trapezoid_method(h)}  m={1 / h}')

print('Формула Грегори:')
gregory_results = []
for h in steps:
    gregory_results.append(get_gregory_method(h))
    print(f'    h={h}   I[f]={get_gregory_method(h)}  m={1 / h}')

print(f'\nПогрешность по Рунге:')
print(f'Метод трапеций:')
print(f'R_0.1 = {(trapezoid_results[0] - trapezoid_results[1]) / 3}')
print(f'R_0.05 = {(trapezoid_results[1] - trapezoid_results[2]) / 3}')
print(f'\nГрегори:')
print(f'R_0.1 = {(gregory_results[0] - gregory_results[1]) / 3}')
print(f'R_0.05 = {(gregory_results[1] - gregory_results[2]) / 3}')

print(f'\nГаусс:')
print(f'I[f]={5 / 18 * f((5 - math.sqrt(15)) / 10) + 5 / 18 * f((5 + math.sqrt(15)) / 10) + 4 / 9 * f(1 / 2)}')

x = symbols('x')
# Определение функции
f = cos(x ** 4)
# Вычисление 6-й производной
sixth_derivative = diff(f, x, 6)

print(f'\n6-я производная: {sixth_derivative}')
