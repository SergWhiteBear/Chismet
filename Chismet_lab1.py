import numpy as np
import math


def series_term1(x):
    return (x + 1) / (x ** 3 + 0.3)


def series_term2(x):
    return (x ** 2 - 0.3) / (x ** 5 + 0.3 * x ** 2)


def series_term3(x):
    return (x**2 - 0.3) / (x ** 5 + 0.3 * x ** 2) - 1 / x**3

# Подсчет ряда 1/n^3
N = 1000
series_sum = 0

for n in range(1, N + 1):
    series_sum += 1 / n ** 3

n1 = 10 ** 7  # Количество членов ряда
n2 = 2237  # Количество членов ряда
n3 = 30  # Количество членов ряда
x = 1

terms1 = np.array([series_term1(i) for i in range(1, n1 + 1)])
terms2 = np.array([series_term2(i) for i in range(1, n2 + 1)])
terms3 = np.array([series_term3(i) for i in range(1, n3 + 1)])
total_sum3 = np.sum(terms3)

total_sum1 = np.sum(terms1)
total_sum2 = np.sum(terms2)

print("1/n^3 = ",  series_sum)
print("Сумма ряда 1:", total_sum1)
print("Сумма рядов 2:", total_sum2 + math.pi ** 2 / 6)
print("Сумма рядов 3:", total_sum3 + math.pi ** 2 / 6 + series_sum)
print("C_n = ", total_sum3)
