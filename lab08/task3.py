"""
Davydov Mikhail IU7-15B
Lab 8 Task 3
Найти столбец, в котором разница между модулями суммы отрицательных и положительных элементов
минимальна
"""
print("Вводите матрицу построчно, разделяя числа пробелом.")
print("Для оконцания ввода введите пустую строку")

mat = []

# Процесс ввода матрицы отличается от предыдущих примеров тем, что при работе
# со столбцами принципиально важно, чтобы матрица была правильной формы и
# не содержала строк разной длины, поэтому после ввода первой строки программа запоминает,
# какой длины должна быть строка и далее может изменять введенные данные, добавляя нули
# или удаляя излишние значения

row_length = 0

while True:
	row_str = input()
	if len(row_str) == 0:
		break

	row = [float(num) for num in row_str.split()]

	if len(row) == 0:
		continue
	
	if len(mat) == 0:
		row_length = len(row)
	
	len_diff = len(row) - row_length
	if len_diff > 0:
		for existing_row in mat:
			existing_row.extend([0.] * len_diff)
		row_length = len(row)
		print("Введенные до этого строки дополнены нулями для соответствия только что введенной")
	if len_diff < 0:
		row.extend([0.] * (-len_diff))
		print("Введенная строка была дополнена нулями для соответствия предыдущим")

	mat.append(row)

# Вывод изначальной	матрицы
for row in mat:
	print("|", ("{:^10.5g}|"*len(row)).format(*row))

col_length = len(mat)

if len(mat) > 0:
	# Проходим по всем столбцам матрицы и считаем суммы их элементов
	#
	#
	# Заметка: разница между модулями сумм положительных 
	# и отрицательных чисел есть просто модуль суммы всех чисел
	# ||S(pos)| - |S(neg|| = |S(pos) + S(neg)| 
	# Знаки модулей у сумм отрицательных и положительных чисел легко раскрыть 
	#
	#
	# Таким образом находим максимальный столбец по данному показателю
	abs_sum_min = float("inf")
	abs_sum_min_col_index = 0
	for i in range(row_length):
		col_sum = 0
		for j in range(col_length):
			col_sum += mat[j][i]
		print(col_sum)
		col_abs_sum = abs(col_sum)
		if col_abs_sum < abs_sum_min:
			abs_sum_min = col_abs_sum
			abs_sum_min_col_index = i

print("Столбец с наименьшей разницей между модулями сумм положительных и"
	 f" отрицательных элементов имеет номер {abs_sum_min_col_index} (с нуля)")
