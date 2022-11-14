"""
Davydov Mikhail IU7-15B
Lab 10
Левые треугольники
3/8
"""
from script import main

def func(arg):
	return arg**3 - arg

def real_a_der(arg):
	return (arg**4)/4 - (arg**2)/2

if __name__ == "__main__":
	main(func, real_a_der)