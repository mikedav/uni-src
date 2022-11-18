"""
Davydov Mikhail IU7-15B
Lab 8 Task 5
Найти максимальное значение в квадратной матрице над главной диагональю и
минимальное - под побочной диагональю.
"""
print("Вводите матрицу построчно, разделяя числа пробелом.")
print("Матрица должна быть квадратной.")

mat = []

mat_size = float("inf")

max_above_main = float("-inf")
min_under_sec = float("inf")

# После ввода строки сразу ищем в нужных областях необходимые минимум и максимум
while len(mat) < mat_size:
	row_str = input()
	row = [float(num) for num in row_str.split()]

	if len(row) == 0:
		continue
	
	if len(mat) == 0:
		mat_size = len(row)
	
	len_diff = len(row) - mat_size
	if len_diff > 0:
		for existing_row in mat:
			existing_row.extend([0.] * len_diff)
		mat_size = len(row)
		print("Введенные до этого строки дополнены нулями для соответствия только что введенной")
	if len_diff < 0:
		row.extend([0.] * (-len_diff))
		print("Введенная строка была дополнена нулями для соответствия предыдущим")

	mat.append(row)
	

for row, index in zip(mat, range(len(mat))):
	if index + 1 < mat_size:
		for num in row[index + 1:]:
			max_above_main = max(num, max_above_main)
	if index > 0:
		for num in row[-index:]:
			min_under_sec = min(num, min_under_sec)

# Остается только вывести матрицу и найденные значения
for row in mat:
	print("|", ("{:^10.5g}|"*len(row)).format(*row))

if mat_size < 2:
	print("Матрица слишком мала для выполнения задания")
	quit()

print(f"Наибольшее значение над главной диагональю: {max_above_main:5g}")
print(f"Наименьшее значение под побочной диагональю: {min_under_sec:5g}")