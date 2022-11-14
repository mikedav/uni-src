def integral_real(start, end, a_der):
	return a_der(end) - a_der(start)

def integral_digital(start, end, num_columns, subject, method):
	int_width = start - end
	col_width = int_width / num_columns
	return sum([method(start + i * col_width, col_width, subject) for i in range(num_columns + 1)])

def m_three_eights(point, width, subject):
	step = width / 3
	return .375 * step * (subject(point) + 3 * subject(point + step) +  3 * subject(point + 2 * step) + subject(point + width))

def m_parabola(point, width, subject):
	step = width / 2
	return (width / 6) * (subject(point) + 4 * subject(point + step) + subject(point + width))

def m_trapezia(point, width, subject):
	return (subject(point) + subject(point + width)) / 2 * width

def m_left_column(point, width, subject):
	return subject(point) * width

def m_right_column(point, width, subject):
	return subject(point + width) * width

def m_mid_column(point, width, subject):
	return (subject(point) + subject(point + width)) / 2 * width