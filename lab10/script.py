import integral as il
import validate as vi
from table import begin_table, add_row

def main(subject, real_a_der):
	sections_num1 = vi.next_natural("Введите первое количество участков разбиения: ")
	sections_num2 = vi.next_natural("Введите второе количество участков разбиения: ")
	interval_start = vi.next_float("Введите начало интервала: ")
	interval_end = vi.next_float_in_range(interval_start, float("inf"), "Введите конечную точку интервала: ")
	eps = vi.next_float("Введите необходимую точность: ")

	eps_zero = 1e-5
	limit_iter = 1e3

	integral_real = il.integral_real(interval_start, interval_end, real_a_der)

	def lc_integral(sections_num):
		return il.integral_digital(interval_start, interval_end, sections_num, subject, il.m_left_column)

	def te_integral(sections_num):
		return il.integral_digital(interval_start, interval_end, sections_num, subject, il.m_three_eights)
	
	def get_abs_err(integral_value):
		abs_err = abs(integral_real - integral_value)
		return abs_err if abs(abs_err) > eps_zero else 0.

	def get_rel_err(abs_err):
		if integral_real != 0.:
			return abs_err/integral_real
		else:
			return "Не вычислено"


	int_values = (lc_integral(sections_num1), lc_integral(sections_num2), te_integral(sections_num1), te_integral(sections_num2))
	abs_err = tuple(map(get_abs_err, int_values))
	rel_err = tuple(map(get_rel_err, abs_err))

	best_method_index = (abs_err.index(min(abs_err))) // 2
	tested_method = (te_integral, lc_integral)[best_method_index]

	delta = float("inf")
	sections_num = 1

	while delta > eps and sections_num < limit_iter:
		delta = abs(tested_method(sections_num) - tested_method(sections_num * 2))
		sections_num += 1



	table = begin_table(3, 25)
	add_row(table, "", f"N1={sections_num1}", f"N2={sections_num2}")
	add_row(table, "Метод левых прямоуг.", int_values[0], int_values[1])
	add_row(table, "Метод 3/8.", int_values[2], int_values[3])
	add_row(table, "Аналит. пол. зн.", integral_real, "")
	add_row(table, "Абс. погр. метода 1", abs_err[0], abs_err[1])
	add_row(table, "Абс. погр. метода 2", abs_err[2], abs_err[3])
	add_row(table, "Отн. погр. метода 1", rel_err[0], rel_err[1])
	add_row(table, "Отн. погр. метода 2", rel_err[2], rel_err[3])

	print(f"Более быстрым оказался метод {('левых прямоугольников', 'трех восьмых')[best_method_index]}")

	if sections_num < 1000:
		print(f"Для менее точного метода необходимо {sections_num} для достижения указанной точности")
	else:
		print(f"Увеличив число интервалов до {limit_iter} указанной точности достичь не удалось")


