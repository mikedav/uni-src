"""
IU7-15B Davydov Mikhail
Lab 4 - Loops v8
"""
import math

# Константы из условия задачи
start_point = .5 # Начало
end_point = 3. # Конец
delta_x = .1 # Шаг

# Базовые рассчеты
interval_length = end_point - start_point # Длина диапазона
num_points = round(interval_length / delta_x) # Число точек

# Маленькое число, нужное, чтобы избегать
# ошибок, связанных с представлением чисел
eps = 1e-5

# Константы, определяющие внешний вид таблицы
row_width = 14 # Ширина одного столбца
table_width = row_width * 3 + 4 # Ширина всей таблицы
table_hor_line = "-" * table_width # Горизонтальная черта
table_line_unformatted = "|{0}|{1}|{2}|" # Рамка таблицы

# Константы, определяющие внешний вид графика
print_width = 85 # Ширина печати
margin_for_x_values = 5 # Ширина поля со значениями x
plot_print_width = print_width - margin_for_x_values # Ширина самого графика

# Установим х в начальную точку
arg_value = start_point

# Для решения доп. задания и построения графика
# необходимо будет найти минимум и максимум функции №2

# Установим изначальное значение минимума
func2_min_value = float("inf")
func2_min_arg = start_point

# А так же начальное значение максимума
func2_max_value = float("-inf")
func2_min_arg = start_point

# Сформируем и напечатаем шапку таблицы
tabletop_x_text = "x".center(row_width)
tabletop_y1_text = "y1".center(row_width)
tabletop_y2_text = "y2".center(row_width)

tabletop_line = table_line_unformatted.format(tabletop_x_text,
    tabletop_y1_text, tabletop_y2_text)

print(table_hor_line)
print(tabletop_line)
print(table_hor_line)

# Условие цикла - дохождение до конца интервала
# При этом программа не посчитает, что вышла за его границы из-за
# ошибок с представлением чисел, благодаря небольшому расширению
# границ диапазона
while arg_value < end_point + eps:
    # Формируем поле таблицы со значением х
    arg_text = f"{arg_value:6g}".center(row_width)

    # Формируем поле таблицы со значением y1
    func1_value = math.sqrt(arg_value) - 2 * math.cos(math.pi / 2 * arg_value)
    func1_text = f"{func1_value:6g}".center(row_width)

    # Формируем поле таблицы со значением y2
    func2_value = math.tan(0.2 * arg_value + 0.3) - arg_value**2 + 3
    func2_text = f"{func2_value:6g}".center(row_width)

    # Проверяем, является ли рассматриваемая точка минимумом
    # или максимумом функции №2
    if func2_value < func2_min_value:
        func2_min_value = func2_value
        func2_min_arg = arg_value

    if func2_value > func2_max_value:
        func2_max_value = func2_value
        func2_max_arg = arg_value

    # Формируем и выводим строку таблицы
    table_line = table_line_unformatted.format(arg_text, func1_text, func2_text)

    print(table_line)

    # Увеличиваем х для следующей итерации
    arg_value += delta_x

# Завершаем таблицу
print(table_hor_line)

print(f"Минимум y2 достигается при x = {func2_min_arg:6g} и равен y2 = {func2_min_value:6g}")

# Запрашиваем ввод числа секций
num_sections = 0

while num_sections > 8 or num_sections < 4:
    num_sections = int(input("Введите число засечек от 4 до 8: "))

# Проводим рассчеты, необходимые для построения графика
value_interval = func2_max_value - func2_min_value # Интервал значений y2
section_length = value_interval / num_sections # Расстояние между "засечками"
# Ширина печати расстояния между засечками
section_print_width = math.floor(plot_print_width / num_sections)
length_per_char = value_interval / plot_print_width # Расстояние на одно знакоместо

# На строке с подписями оси ординат делаем отступ
legend_y = " " * margin_for_x_values

# Формируем подписи на "засечках"
for i in range(num_sections):
    section_marker = func2_min_value + i * section_length
    legend_y += f"{section_marker:6g}".center(section_print_width)

# Выводим подписи
print(legend_y)

arg_value = start_point

# Выясняем, нужно ли проводить черту на графике, и рассчитываем ее место
is_crossing_zero = func2_max_value > 0 > func2_min_value
if is_crossing_zero:
    ver_line_index = math.floor(-func2_min_value / length_per_char)

while arg_value < end_point + eps:
    # Повторно вычисляем y2
    func2_value = math.tan(0.2 * arg_value + 0.3) - arg_value**2 + 3

    # Начинаем формировать строку графика
    plot_line = " " * plot_print_width

    # При необходимости нужный пробел заменяем верт. чертой
    if is_crossing_zero:
        # Пробел именно заменяется, а не вставляется, так как второй слайс,
        # на который мы делим строку, взят со следующего символа
        plot_line = plot_line[:ver_line_index] + "|" + plot_line[ver_line_index + 1:]

    # Вычисляем место звездочки в строке, и заменяем ей нужный пробел
    func2_on_interval = func2_value - func2_min_value
    asterisk_index = math.floor(func2_on_interval / length_per_char)

    plot_line = plot_line[:asterisk_index] + "*" + plot_line[asterisk_index + 1:]

    # Добавляем подпись со значением х
    legend_x = f"{arg_value:6g}|".rjust(margin_for_x_values)

    print(legend_x + plot_line)

    arg_value += delta_x
