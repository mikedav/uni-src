"""
Davydov Mikhail IU7-15B
Lab 7 Task 1
Удалить все нулевые элементы
"""
data = list(map(int, input("Введите целочисленный список через пробел: ").split()))

# data = filter(lambda x : x != 0, data)

null_count = 0
i = 0

# Если мы дошли до конца списка, выходим из цикла
while i + null_count < len(data):
	# Если элемент равен нулю, увеличиваем сдвиг
	if data[i + null_count] == 0:
		null_count += 1
	# Проверка нужна на случай, если нулевым окажется последний элемент -
	# тогда дать ему значение следующего не получится
	if i + null_count < len(data):
		data[i] = data[i + null_count]
	i += 1 

# Обрезаем список до нужной длины
data = data[:-null_count]

print(*data)