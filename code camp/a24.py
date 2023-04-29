import math
import matplotlib.pyplot as plt


def price(A, B, C, x1, x2):

  def curve(x):
    return A * x**2 + B * x + C

  if x1 > x2:
    x1, x2 = x2, x1

  area = 0
  for x in [x1, x2]:
    area += math.pi * curve(x)**2

  dx = 0.01
  for x in [x1 + dx * i for i in range(int((x2 - x1) / dx))]:
    area += math.pi * (curve(x)**2 - curve(x - dx)**2)

  return area


def calculate_volume(A, B, C, volume):

  def curve(x):
    return A * x**2 + B * x + C

  def integral(x):
    return math.pi * curve(x)**2

  def volume_error(x):
    return abs(volume - 2 * quad(integral, 0, x)[0])

  from scipy.integrate import quad
  from scipy.optimize import minimize_scalar

  x_max = minimize_scalar(volume_error, bounds=(0, 10)).x
  x1 = -x_max
  x2 = x_max

  return (x1, x2)


def plot_vase(A, B, C, x1, x2):
  """Plot the profile of a vase given its quadratic function and endpoints."""

  def curve(x):
    return A * x**2 + B * x + C

  xs = [x1 + (x2 - x1) * i / 100 for i in range(101)]
  ys = [curve(x) for x in xs]

  plt.plot(xs, ys)
  plt.show()


#Example:
A, B, C, x1, x2 = 1, 0, 0, 0, 1
price1 = price(A, B, C, x1, x2)


volume = math.pi / 2
x1, x2 = calculate_volume(A, B, C, volume)
plot_vase(A, B, C, x1, x2)

print(f"Price: {price1}")
print(f"Volume endpoints: ({x1}, 0), ({x2}, 0)")


