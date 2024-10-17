from scipy import integrate
import numpy as np

def my_func(x):
    return x**2

integral = integrate.quad(my_func, 0, 1)
print(integral)