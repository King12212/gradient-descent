import math

def f(x):
    return 3 * x**2 + 2 * x + 4 * math.sin(x)

def df(x):
    return 6 * x + 2 + 4 * math.cos(x)

def gradient_descent(x0, learning_rate, num_iterations):
    x = x0
    for i in range(num_iterations):
        grad = df(x)
        x_new = x - learning_rate * grad
        if abs(x_new - x) < 1e-2: 
            return x_new, i + 1
        x = x_new
    return x, num_iterations

x0 = -5
learning_rate = 0.1
num_iterations = 100

x_min, iterations = gradient_descent(x0, learning_rate, num_iterations)

print(f"{x_min:.6f}")
print(f"{f(x_min):.6f}")
print(f"{iterations}")