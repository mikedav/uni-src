"""
Davydov Mikhail IU7-15B
Lab 7 Task 4
Замена всех гласных на заглавные
"""
from abcdata import vowels

data = []
input_terminator = "/end"
input_prompt = f"Введите строку ({input_terminator} для завершения ввода): "

while True:
	string = input(input_prompt)
	if string.startswith(input_terminator):
		break
	data.append(string)

# Поочередно формируем новые строки и заменяем ими элементы массива
for i in range(len(data)):
	replacement = ""
	for character in data[i]:
		replacement += character if character not in vowels else character.upper()
	data[i] = replacement
	print(data[i])