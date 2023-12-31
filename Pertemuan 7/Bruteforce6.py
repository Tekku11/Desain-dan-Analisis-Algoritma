# Menghitung Polynomial (Slide 25)
def polynomial_py(a, x):
    result = 0
    # for every n in 0..len(a) - 1
    for n, a_n in enumerate(a):
        # compute x^n
        x_power_n = 1
        for i in range(n):
            x_power_n = x_power_n * x
        # add a_n * x^n to the final result
        result = result + a_n * x_power_n
    return result

a = [1, 2, 0, 3] # coefficients
x = 1.5
print(polynomial_py(a, x)) # 14.125