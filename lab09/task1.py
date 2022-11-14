"""
Davydov Mikhail IU7-15B
Lab 9 Task 1 
"""
from math import sin

d_arr = list(map(float, input("Введите массив D через пробел:\n").split()))
f_arr = list(map(float, input("Введите массив F через пробел:\n").split()))

a_mat = []
av_arr = []
l_arr = []

if len(d_arr) < 0 or len(f_arr) < 0:
	print("Оба массива не должны быть пустыми")
	quit()

for dj in d_arr:
	new_row = [sin(dj + fk) for fk in f_arr]
	avg = sum(new_row) / len(new_row)
	av_arr.append(avg)
	l_arr.append(len(list(filter(lambda x : x < avg, new_row))))
	a_mat.append(new_row)

table_header = " " * (1 + 11*len(f_arr)) + "{:^10} {:^10} ".format("AV", "L") 

print(table_header)
for row, avg, lower_than_avg in zip(a_mat, av_arr, l_arr):
	print("|", ("{:^10.5g}|"*len(row)).format(*row), f"{avg:^10.5g}|", f"{lower_than_avg:^10.5g}|", sep="")