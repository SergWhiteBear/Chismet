

def Jacobi():
    epsilon = 0.00005

    n = 0
    x1_prev = 0
    x2_prev = 0
    x3_prev = 0
    x1 = 2.27 / 1.69
    x2 = 2.66 / 0.81
    x3 = 4.74
    while abs(x1 - x1_prev) > epsilon and abs(x2 - x2_prev) > epsilon \
            and abs(x3 - x3_prev) > epsilon:
        n += 1
        x1_prev = x1
        x2_prev = x2
        x3_prev = x3
        x1 = (2.27 + 0.01 * x2_prev - 0.2 * x3_prev) / 1.69
        x2 = (2.66 + 0.1 * x1_prev - 0.38 * x3_prev) / 0.81
        x3 = (4.74 - 0.22 * x1_prev - 0.76 * x2_prev)

    print(f'x1 = {x1}, x2 = {x2}, x3 = {x3}, n = {n}')


def gauss_seidel():
    epsilon = 0.00005

    n = 0
    x1_prev = 0
    x2_prev = 0
    x3_prev = 0
    x1 = 2.27 / 1.69
    x2 = 2.66 / 0.81
    x3 = -2.37 / -0.5
    while abs(x1 - x1_prev) > epsilon and abs(x2 - x2_prev) > epsilon \
            and abs(x3 - x3_prev) > epsilon:
        n += 1
        x1_prev = x1
        x2_prev = x2
        x3_prev = x3
        x1 = (2.27 + 0.01 * x2_prev - 0.2 * x3_prev) / 1.69
        x2 = (2.66 + 0.1 * x1 - 0.38 * x3_prev) / 0.81
        x3 = (-2.37 + 0.11 * x1 + 0.38 * x2) / -0.5

    print(f'x1 = {x1}, x2 = {x2}, x3 = {x3}, n = {n}')

if __name__ == '__main__':
    Jacobi()
    gauss_seidel()
