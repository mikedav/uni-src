"""
Davydov Mikhail IU7-15B
Lab 10
Левые треугольники
3/8
"""
import integral as il

def func(arg):
	return arg**3 - arg

def real_a_der(arg):
	return (arg**4)/4 - (arg**2)/2

print(il.integral_real(0, 1, real_a_der))
print(il.integral_digital(0, 1, 40, func, il.m_left_column))
print(il.integral_digital(0, 1, 40, func, il.m_three_eights))