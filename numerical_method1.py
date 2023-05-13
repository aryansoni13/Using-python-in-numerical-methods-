import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 2*x - 5

def f_derivative(x):
    return 3*x**2 - 2

def newton_raphson(guess, tolerance=0.0001, max_iterations=100):
    x = guess
    iterations = 0
    data = [(x, f(x))]
    
    while abs(f(x)) > tolerance and iterations < max_iterations:
        x = x - f(x) / f_derivative(x)
        iterations += 1
        data.append((x, f(x)))
    return x, data

initial_guess = float(input())
print("Initial guess is: ",initial_guess)
root, iterations_data = newton_raphson(initial_guess)
print("Root:", root)
print("Iterations:")
for iteration, (x, fx) in enumerate(iterations_data):
    print(f"Iteration {iteration + 1}: x = {x}, f(x) = {fx}")

x_vals = np.linspace(-10, 10, 400)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label='f(x) = x^3 - 2x - 5')
x_iterations = [x for x, _ in iterations_data]
y_iterations = [fx for _, fx in iterations_data]
plt.plot(x_iterations, y_iterations, 'ro', label='Iterations')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Newton-Raphson Method')
plt.grid(True)
plt.show()