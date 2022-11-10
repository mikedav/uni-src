"""
Davydov Mikhail IU7-15B
Lab 8 Task 2
переставить местами строки с наибольшим и наименьшим числом отр чисел
"""
print("Вводите матрицу построчно, разделяя числа пробелом.")
print("Для оконцания ввода введите пустую строку")

mat = []

# Устанавливаем переменные для поиска необходимых строк заранее, 
# так как искать их будет сразу после ввода
min_neg_count = float("inf")
max_neg_count = float("-inf")
max_neg_count_index = 0
min_neg_count_index = 0

while True:
	row_str = input()
	if len(row_str) == 0:
		break

	row = [float(num) for num in row_str.split()]
	
	if len(row) == 0:
		continue

	mat.append(row)

	# Считаем отрицательные числа в введенной строке матрицы
	neg_count = 0
	for num in row:
		neg_count += num < 0

	# Проверяем, не является ли строка максимальной или 
	# минимальной по этому показателю
	if neg_count > max_neg_count:
		max_neg_count = neg_count
		max_neg_count_index = len(mat) - 1

	if neg_count < min_neg_count:
		min_neg_count = neg_count
		min_neg_count_index = len(mat) - 1

# Выводим изначальную матрицу,
# меняем строки местами,
# Выводим результат
if len(mat) > 0:
	for row in mat:
		print("|", ("{:^10.5g}|"*len(row)).format(*row))

	mat[min_neg_count_index], mat[max_neg_count_index] = mat[max_neg_count_index], mat[min_neg_count_index]
	
	print("\n\n")
	for row in mat:
		print("|", ("{:^10.5g}|"*len(row)).format(*row))


