"""
Davydov Mikhail IU7-15B
Lab 8 Task 6
Выполнить транспонирование квадратной матрицы.
"""
print("Вводите матрицу построчно, разделяя числа пробелом.")
print("Матрица должна быть квадратной.")

mat = []

mat_size = float("inf")

max_above_main = float("-inf")
min_under_sec = float("inf")

while len(mat) < mat_size:
	row_str = input()
	row = [float(num) for num in row_str.split()]

	if len(row) == 0:
		continue
	
	if len(mat) == 0:
		mat_size = len(row)
	
	len_diff = len(row) - mat_size
	if len_diff > 0:
		row = row[:-len_diff]
		print("Введенная строка была обрезана для соответствия предыдущим")
	if len_diff < 0:
		row.extend([0.] * (-len_diff))
		print("Введенная строка была дополнена нулями для соответствия предыдущим")

	mat.append(row)

for row in mat:
	print("|", ("{:^10.5g}|"*len(row)).format(*row))

print("\n\n")

# Все числа под главной диагональю меняем местами с соответствующими им при транспонировании
for i in range(mat_size):
	for j in range(i + 1, mat_size):
		mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

for row in mat:
	print("|", ("{:^10.5g}|"*len(row)).format(*row))
