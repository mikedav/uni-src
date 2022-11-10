"""
Davydov Mikhail IU7-15B
Lab 7 Task 3 
Поиск элемента с наибольшим числом английских согласных букв
"""
from abcdata import consonants

data = []
input_terminator = "/end"
input_prompt = f"Введите строку ({input_terminator} для завершения ввода): "

# Сразу после ввода будем считать согласные и искать максимум
max_cons_count = 0
max_cons_count_index = 0

while True:
	string = input(input_prompt)
	if string.startswith(input_terminator):
		break
	data.append(string)
	cons_count = 0
	for character in string.lower():
		if character in consonants:
			cons_count += 1
	if cons_count > max_cons_count:
		max_cons_count = cons_count
		max_cons_count_index = len(data) - 1


if len(data) > 0:
	print(data[max_cons_count_index])
else:
	print("Вы не ввели ни одной строки. Надо же...")
