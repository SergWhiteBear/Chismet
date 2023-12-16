import numpy as np
import math


def series_term1(x):
    return (x + 1) / (x ** 3 + 0.3)


def series_term2(x):
    return (x ** 2 - 0.3) / (x ** 5 + 0.3 * x ** 2)


def series_term3(x):
    return (-3 * (x + 1)) / (10 * x ** 6 + 3 * x ** 2)

# Подсчет ряда 1/n^3
N = 2000
series_sum = 0

for n in range(1, N + 1):
    series_sum += 1 / n ** 3

n1 = 10 ** 7  # Количество членов ряда
n2 = 2237  # Количество членов ряда
n3 = 30  # Количество членов ряда
x = 1  # Замените на нужное значение x

# Генерируем массив значений членов ряда
terms1 = np.array([series_term1(i) for i in range(1, n1 + 1)])
terms2 = np.array([series_term2(i) for i in range(1, n2 + 1)])
terms3 = np.array([series_term3(i) for i in range(1, n3 + 1)])

total_sum1 = np.sum(terms1)
total_sum2 = np.sum(terms2)
total_sum3 = np.sum(terms3)

print("Сумма ряда 1:", total_sum1)
print("Сумма рядов 2:", total_sum2 + math.pi ** 2 / 6)
print("Сумма рядов 3:", total_sum3 + math.pi ** 2 / 6 + series_sum)
print("SUm3", total_sum3)


# Так искал корень для последнего неравенства
l = 100
for k in range(1, l + 1):
    res = 3 / (40 * k ** 4) + 3 / (50 * k ** 5)
    if res <= 1 / 10 ** 7:
        print(k, res)
        break
