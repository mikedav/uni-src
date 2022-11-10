"""
Davydov Mikhail IU7-15B
Lab 8 Task 1 v. 1 3
Найти строку с наибольшим средним арифметическим
"""

print("Вводите матрицу построчно, разделяя числа пробелом.")
print("Для оконцания ввода введите пустую строку")

mat = []

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

# Устанавливаем изначальные значения
max_avg = float("-inf")
max_avg_index = 0
# Проходим по строкам матрицы и их индексам
for row, num_row in zip(mat, range(len(mat))):
	# Ищем среднее арифметическое с помощью встроенных функций
	avg = sum(row) / len(row)
	# Радуемся, если нашли очередной максимум
	if avg > max_avg:
		max_avg = avg
		max_avg_index = num_row
	# Выводим строку матрицы в том же цикле
	print(f"Строка {num_row:<5.3g}|", ("{:^10.5g}|"*len(row)).format(*row), f" Ср. ар: {avg:5g}")

if len(mat) > 0:
	print(f"Строка с максимальным средним арифметическим имеет номер {max_avg_index} (с нуля)")
