"""
Lab 04 Защита

постр график
-x**2 + 4
без табл 
без засечек
"""
import math

start_point = float(input("Введите начальную точку интервала: "))
end_point = float(input("Введите конечную точку интервала: "))
delta_x = float(input("Введите шаг: "))

plot_width = 80
margin_width = 10


eps = 1e-5

arg_value = start_point

min_y = float("inf")
max_y = float("-inf")

while arg_value < end_point + eps:
    func_value = -arg_value**2 + 4
    
    if func_value > max_y:
        max_y = func_value

    if func_value < min_y:
        min_y = func_value

    arg_value += delta_x

func_interval = max_y - min_y
length_per_char = func_interval / plot_width

crosses_OX = max_y >= 0 >= min_y
if crosses_OX:
    ver_line_index = math.floor(-min_y / length_per_char)

arg_value = start_point

while arg_value < end_point + eps:
    line = " " * plot_width

    if crosses_OX:
        line = line[:ver_line_index] + "|" + line[ver_line_index + 1:]
    
    func_value = -arg_value**2 + 4


    asterisk_index = math.floor((func_value - min_y) / length_per_char)

    line = line[:asterisk_index] + "*" + line[asterisk_index + 1:]

    if abs(arg_value) < eps:
        arg_value = 0.

    legend = f"{arg_value:>{margin_width}.2g}|"

    print(legend + line)
    arg_value += delta_x