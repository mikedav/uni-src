"""
IU7-15B Davydov Mikhail
Lab 5 - Calc Sum v8
"""
import math


num_iter = 1

row_width = 10
num_columns = 3
hor_line = "-" * ((row_width + 1) * num_columns + 1)
table_line = "|" + "{}|" * num_columns
table_cell = f"{{:>{row_width}.6g}}"
tcf = table_cell.format

arg_value = float(input("Введите значение аргумента: "))
eps = float(input("Введите точность: "))
max_iter_num = int(input("Введите максимиальное число итераций: "))
print_step = int(input("Введите шаг печати: "))

sum_value = 0.
multiplier = (arg_value - 1) / arg_value
last_value_no_n_division = multiplier
cur_value = multiplier
iter_num = 1

print(hor_line)
print(table_line.format(tcf("№ итерации")), tcf("t"), tcf("s"))
print(hor_line)
while iter_num < max_iter_num and cur_value >= eps:
	cur_value = last_value_no_n_division / iter_num
	sum_value += cur_value
	if num_iter % print_step == 0:
		print(table_line.format(tcf(num_iter), tcf(cur_value), tcf(sum_value)))
		print(hor_line)
	iter_num += 1
	last_value_no_n_division *= multiplier
	
if cur_value < eps:
	print(f"Сумма бесконечного ряда - {sum_value}, вычислена за {num_iter - 1} итераций.")
else:
	print("За указанное число итераций необходимой точности достичь не удалось.")
	
