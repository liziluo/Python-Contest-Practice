import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

def curve(x, a, b, c):
    return a * x**2 + b * x + c

def area(x, a, b, c):
    return (a * x**3 / 3) + (b * x**2 / 2) + (c * x)

def vase_volume(x, a, b, c):
    return (a * x**5 / 5) + (b * x**4 / 4) + (c * x**3 / 3)

def price(x1, x2, a, b, c):
    return area(x2, a, b, c) - area(x1, a, b, c)

def find_symmetric_x(volume, a, b, c):
    x_max = minimize_scalar(lambda x: -curve(x, a, b, c)).x
    target_volume = volume / 2
    left_x = minimize_scalar(lambda x: abs(vase_volume(x_max, a, b, c) - vase_volume(x, a, b, c) - target_volume)).x
    right_x = minimize_scalar(lambda x: abs(vase_volume(x, a, b, c) - vase_volume(x_max, a, b, c) - target_volume)).x
    return left_x, right_x

def plot_vase_profile(a, b, c, x1, x2):
    x = np.linspace(x1, x2, 100)
    y = curve(x, a, b, c)
    plt.plot(x, y)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Vase Profile')
    plt.show()

# Example inputs
a, b, c = 1, 2, 1
x1, x2 = 1, 2

# 1. Price
print("Price:", price(x1, x2, a, b, c))

# 2. Volume
print("Volume:", vase_volume(x2, a, b, c) - vase_volume(x1, a, b, c))

# 3. Symmetric vase
volume = 10
x1, x2 = find_symmetric_x(volume, a, b, c)
print("Symmetric vase endpoints:", x1, x2)

# 4. Plot the profile
plot_vase_profile(a, b, c, x1, x2)
