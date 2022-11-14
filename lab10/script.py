import integral as il
import validate as vi
from table import begin_table, add_row

def main(subject, real_a_der):
	sections_num1 = vi.next_natural("Введите первое количество участков разбиения: ")
	sections_num2 = vi.next_natural("Введите второе количество участков разбиения: ")
	interval_start = vi.next_float("Введите начало интервала: ")
	interval_end = vi.next_float_in_range(interval_start, float("inf"), "Введите конечную точку интервала: ")
	eps = vi.next_float("Введите необходимую точность: ")

	integral_real = il.integral_real(interval_start, interval_end, real_a_der)
	
	integral_left_n1 = il.integral_digital(interval_start, interval_end, sections_num1, subject, il.m_left_column)
	integral_left_n2 = il.integral_digital(interval_start, interval_end, sections_num2, subject, il.m_left_column)
	integral_three_eights_n1 = il.integral_digital(interval_start, interval_end, sections_num1, subject, il.m_three_eights)
	integral_three_eights_n2 = il.integral_digital(interval_start, interval_end, sections_num2, subject, il.m_three_eights)
	
	abs_err_left_n1 = abs(integral_real - integral_left_n1)
	abs_err_left_n2 = abs(integral_real - integral_left_n2)
	abs_err_three_eights_n1 = abs(integral_real - integral_three_eights_n1)
	abs_err_three_eights_n2 = abs(integral_real - integral_three_eights_n2)

	rel_err_left_n1 = abs_err_left_n1 / integral_real
	rel_err_left_n1 = abs_err_left_n2 / integral_real
	rel_err_three_eights_n1 = abs_err_three_eights_n1 / integral_real
	rel_err_three_eights_n1 = abs_err_three_eights_n2 / integral_real

	table = begin_table(3, 25)
	add_row(table, "", f"N1={sections_num1}", f"N2={sections_num2}")
	add_row(table, "Метод левых прямоуг.", f"{integral_left_n1:6g}", f"{integral_left_n2:6g}")
	add_row(table, "Метод 3/8.", f"{integral_three_eights_n1:6g}", f"{integral_three_eights_n2:6g}")
	add_row(table, "Аналит. пол. зн.", f"{integral_real:6g}", "")
	add_row(table, "Абс. погр. метода 1", f"{abs_err_left_n1:6g}", f"{abs_err_left_n2:6g}")
	add_row(table, "Абс. погр. метода 2", f"{abs_err_three_eights_n1:6g}", f"{abs_err_three_eights_n2:6g}")
	add_row(table, "Отн. погр. метода 1", f"{rel_err_left_n1:6g}", f"{rel_err_left_n2:6g}")
	add_row(table, "Отн. погр. метода 2", f"{rel_err_three_eights_n1:6g}", f"{rel_err_three_eights_n2:6g}")

	
	