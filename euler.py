import numpy as np
import matplotlib.pyplot as plt

y0 = 1
t0 = 0
T = 1
h = 0.2

# Define the differential equation dy/dt = f(t, y)
def f(t, y):
    return 2 * y - 10 * t**2 + 2 * t

# Define the exact solution for comparison
def exact_solution(t):
    return 5 * t**2 + 4 * t + 2 - np.exp(2 * t)

# Number of steps
n = int(np.floor(T / h))

# Arrays to store t and y values
t = np.zeros(n + 1)
z = np.zeros(n + 1)

t[0] = t0
z[0] = y0

for i in range(n):
    z[i + 1] = z[i] + h * f(t[i], z[i])
    t[i + 1] = t0 + (i + 1) * h

# Plot exact and approximate solutions
tt = np.linspace(t0, T, 100)
y_exact = exact_solution(tt)

plt.plot(tt, y_exact, '-b', linewidth=1.5, label='Exact solution')
plt.plot(t, z, '-ro', markerfacecolor='r', linewidth=2, label='Approximate solution')
plt.legend(loc='upper left')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Euler\'s Method Approximation')
plt.savefig('euler_method_plot.png')
