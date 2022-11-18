"""
Вычисление интегралов
"""

# Вычисление интеграла с помощью первообразной
def integral_real(start, end, a_der):
	return a_der(end) - a_der(start)

# Вычисление интеграла с помощью численных методов
def integral_digital(start, end, num_columns, subject, method):
	int_width = end - start
	col_width = int_width / num_columns
	try:
		int_value = sum([method(start + i * col_width, col_width, subject) for i in range(num_columns)])
	except:
		return None
	return int_value

# Метод 3/8
def m_three_eights(point, width, subject):
	step = width / 3
	return .375 * step * (subject(point) + 3 * subject(point + step) +  3 * subject(point + 2 * step) + subject(point + width))

# Метод симпсона
def m_parabola(point, width, subject):
	step = width / 2
	return (width / 6) * (subject(point) + 4 * subject(point + step) + subject(point + width))

# Метод трапеций
def m_trapezia(point, width, subject):
	return (subject(point) + subject(point + width)) / 2 * width

# Метод левых прямоугольников
def m_left_column(point, width, subject):
	return subject(point) * width

# Метод правых прямоугольников
def m_right_column(point, width, subject):
	return subject(point + width) * width

# Метод срединных прямоугольников
def m_mid_column(point, width, subject):
	return subject(point + width / 2) / 2 * width