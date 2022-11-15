"""
Davydov Mikhail IU7-15B
Lab 10
Левые треугольники
3/8
"""
import math
from script import main

def line(x):
	return x

def line_a_der(x):
	return 0.5 * x**2

def quadratic(x):
	return x**2 - 5*x + 3

def quadratic_a_der(x):
	return 1/3*x**3 - 5/2*x**2 + 3*x

def poly5(x):
	return 6*x**5 + 5*x**4 + 4*x**3 + 3*x**2 + 2*x + 1

def poly5_a_der(x):
	return x**6 + x**5 + x**4 + x**3 + x**2 + x

if __name__ == "__main__":
	main(poly5, poly5_a_der)