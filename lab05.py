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

arg_value = float(input("Введите значение аргумента: \n"))
eps = float(input("Введите точность: \n"))
max_iter_num = int(float(input("Введите максимиальное число итераций: \n")))
print_step = int(float(input("Введите шаг печати: \n")))

if eps <= 0.:
	print("Точность должна превышать 0")
	quit()

if arg_value <= 0.:
	print("Значение аргумента должно превышать 0")
	quit()
# Устанавливаем изначальные значения переменных, необходимых
# для вычислений
sum_value = 0.
multiplier = (arg_value - 1) / arg_value
last_value_no_n_division = multiplier
cur_value = float("inf")
iter_num = 1

# Печатаем шапку таблицы
print(hor_line)
print(f"|{'N итерации':>{column_width}}|{'t':>{column_width}}|{'s':>{column_width}}|")
print(hor_line)
# Условие цикла - либо достигнуто макс. число итераций
# либо достигнута необходимая точность
while (iter_num <= max_iter_num) and (cur_value >= eps):
	cur_value = last_value_no_n_division / iter_num
	sum_value += cur_value
	# При прохождении шага печати
	if iter_num % print_step == 0 or iter_num == 1:
		print(table_line.format(tcf(iter_num), tcf(cur_value), tcf(sum_value)))
		print(hor_line)
	iter_num += 1
	last_value_no_n_division *= multiplier
	
if cur_value < eps:
	print(f"Сумма бесконечного ряда - {sum_value:6g}, вычислена за {iter_num - 1} итераций.")
else:
	print("За указанное число итераций необходимой точности достичь не удалось.")
	
