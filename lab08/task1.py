"""
Davydov Mikhail IU7-15B
Lab 8 Task 1 v. 1 3
Найти строку с наибольшим средним арифметическим
"""

print("Вводите матрицу построчно, разделяя числа пробелом.")
print("Для оконцания ввода введите пустую строку")

mat = []

while True:
	row_str = input()
	if len(row_str) == 0:
		break

	row = [float(num) for num in row_str.split()]

	if len(row) == 0:
		continue

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
	print(f"Строка {num_row:<5.3g}|", ("{:^10.5g}|"*len(row)).format(*row), f" Ср. ар: {avg}")

if len(mat) > 0:
	print(f"Строка с максимальным средним арифметическим имеет номер {max_avg_index} (с нуля)")
