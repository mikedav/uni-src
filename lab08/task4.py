"""
Davydov Mikhail IU7-15B
Lab 8 Task 4
Переставить местами столбцы с максимальной и минимальной суммой элементов.
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

col_length = len(mat)

# Ищем нужные стлобцы аналогичным предыдущему заданию образом
min_col_sum = float("inf")
min_col_sum_index = 0
max_col_sum = float("-inf")
max_col_sum_index = 0

for i in range(row_length):
	col_sum = 0.
	for j in range(col_length):
		col_sum += mat[j][i]
	if col_sum > max_col_sum:
		max_col_sum = col_sum
		max_col_sum_index = i
	if col_sum < min_col_sum:
		min_col_sum = col_sum
		min_col_sum_index = i

# Выводим изначальную матрицу
for row in mat:
	print("|", ("{:^10.5g}|"*len(row)).format(*row))

# В каждой строке меняем местами элементы из нужных столбцов
for i in range(col_length):
	mat[i][min_col_sum_index], mat[i][max_col_sum_index] = mat[i][max_col_sum_index], mat[i][min_col_sum_index]

print("\n\n")

# Выводим результат
for row in mat:
	print("|", ("{:^10.5g}|"*len(row)).format(*row))