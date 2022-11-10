"""
Davydov Mikhail IU7-15B
Lab 9 Task 2 
"""
print("Вводите матрицу построчно, разделяя числа пробелом.")
print("Матрица должна быть квадратной.")

mat = []

mat_size = float("inf")

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

for i in range(mat_size // 2):
	for j in range(i, mat_size - i - 1):
		mat[j][-i - 1], mat[-i - 1][-j - 1], mat[-j - 1][i], mat[i][j] = \
			mat[i][j], mat[j][-i - 1], mat[-i - 1][-j - 1], mat[-j - 1][i]

print("\n\n")

for row in mat:
	print("|", ("{:^10.5g}|"*len(row)).format(*row))


for i in range(mat_size // 2):
	for j in range(i, mat_size - i - 1):
		mat[i][j], mat[j][-i - 1], mat[-i - 1][-j - 1], mat[-j - 1][i] = \
			mat[j][-i - 1], mat[-i - 1][-j - 1], mat[-j - 1][i], mat[i][j]


print("\n\n")

for row in mat:
	print("|", ("{:^10.5g}|"*len(row)).format(*row))

