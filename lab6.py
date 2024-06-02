import numpy as np
from matplotlib import pyplot as plt

epsilon = 10 ** -5
A, B = 0, 1


def analytic_solution(x):
    return np.exp(-x) + np.exp(x) + 3.9 * x ** 2 - 3.9 * x - 2


def get_three_Teylor(x_k, y_k, u_k, h):
    y_next = y_k + h * u_k + h ** 2 / 2 * (y_k + 9.8 + 3.9 * x_k * (1 - x_k)) + h ** 3 / 6 * (
            3.9 - 7.8 * x_k + u_k + u_k)
    u_next = u_k + h * (y_k + 9.8 + 3.9 * x_k * (1 - x_k)) \
             + h ** 2 / 2 * (3.9 - 7.8 * x_k + 1 * (y_k + 9.8 + 3.9 * x_k * (1 - x_k))) \
             + h ** 3 / 6 * (-7.8 + 1 * (3.9 - 7.8 * x_k) + 1 * (y_k + 9.8 + 3.9 * x_k * (1 - x_k)))
    return y_next, u_next


def find_y(mu, N, h):
    y = mu
    u = mu - 3.9
    all_y = [y]
    for i in range(N):
        y, u = get_three_Teylor(h * i, y, u, h)
        all_y.append(y)
    return all_y


def phi(y):
    return y - np.e - 1 / np.e + 2


def get_hords(mu_0, mu_1):
    mu_prev = mu_1
    while True:
        mu_k = mu_prev - (phi(mu_prev) / (phi(mu_prev) - phi(mu_0))) * (mu_prev - mu_0)
        if abs(mu_k - mu_prev) < epsilon:
            break
        mu_prev = mu_k
    return mu_k


def get_lambda(A_i, lambda_i):
    return 1 / (A_i - lambda_i)


def get_mu():
    return 1 + 1 / np.e - 2


def tridiagonal(h, N):
    y = np.zeros(N)
    lambdas = np.zeros(N)

    A_i = np.zeros(N)
    A_i[0] = 1 + h
    for n in range(1, N):
        A_i[n] = 1
    A_i[N] = 0
    lambdas[0] = 1 / (1 + h)
    y[N] = get_mu()

    for i in range(0, N):
        lambdas[i + 1] = get_lambda(A_i[i], lambdas[i])

    print(y)

    return y


# Поиск начальных мю: mu_0 и mu_1
def search_bounds(start=-100):
    while phi(start) < 0:
        start += 1
    return start - 1, start


if __name__ == "__main__":
    Nums = [10, 20]
    for N in Nums:
        h = (B - A) / (N - 1)
        x = np.linspace(0.0, 1.0, num=N + 1)

        analytic_solutions = [analytic_solution(x_i) for x_i in x]
        mu_0, mu_1 = search_bounds(-1)
        print(f'mu_0 = {mu_0}; mu_1 = {mu_1}')
        mu = get_hords(mu_0, mu_1)
        # mu = 1.0861612696304874

        y = find_y(mu, N, h)
        print(f'mu = {mu}\nphi(mu) = {phi(mu)}')

        plt.title(f'N={N}')
        plt.plot(x, y, label="Shooting method")
        plt.plot(x, analytic_solutions, label="Reference")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()
