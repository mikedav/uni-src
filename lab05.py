"""
IU7-15B Davydov Mikhail
Lab 5 - Calc Sum v8
"""
import math

# Зададим константы и строки для удобства печати таблицы
column_width = 12
num_columns = 3
hor_line = "-" * ((column_width + 1) * num_columns + 1)
table_line = "|" + "{}|" * num_columns
table_cell = f"{{:>{column_width}.5g}}"
# Сохраняем метод для удобного обращения
tcf = table_cell.format

arg_value = float(input("Введите значение аргумента: "))
eps = float(input("Введите точность: "))
max_iter_num = int(input("Введите максимиальное число итераций: "))
print_step = int(input("Введите шаг печати: "))

# Устанавливаем изначальные значения переменных, необходимых
# для вычислений
sum_value = 0.
multiplier = (arg_value - 1) / arg_value
last_value_no_n_division = multiplier
cur_value = multiplier
iter_num = 1

# Печатаем шапку таблицы
print(hor_line)
print(f"|{'N итерации':>{column_width}}|{'t':>{column_width}}|{'s':>{column_width}}|")
print(hor_line)
# Условие цикла - либо достигнуто макс. число итераций
# либо достигнута необходимая точность
while (iter_num < max_iter_num) and (cur_value >= eps):
	cur_value = last_value_no_n_division / iter_num
	sum_value += cur_value
	# При прохождении шага печати
	if (iter_num - 1) % print_step == 0:
		print(table_line.format(tcf(iter_num), tcf(cur_value), tcf(sum_value)))
		print(hor_line)
	iter_num += 1
	last_value_no_n_division *= multiplier
	
if cur_value < eps:
	print(f"Сумма бесконечного ряда - {sum_value}, вычислена за {iter_num - 1} итераций.")
else:
	print("За указанное число итераций необходимой точности достичь не удалось.")
	
