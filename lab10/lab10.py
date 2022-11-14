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

if __name__ == "__main__":
	main(line, line_a_der)
	main(quadratic, quadratic_a_der)
	main(math.sin, math.cos)