"""
IU7-15B Davydov Mikhail Triangle Math
"""
import math
import sys

# Запрашиваем ввод координат вершин треугольника
print("Назовем треугольник АВС.")
A_x = int(input("Введите координату Х точки А: "))
A_y = int(input("Введите координату Y точки А: "))
B_x = int(input("Введите координату Х точки B: "))
B_y = int(input("Введите координату Y точки B: "))
C_x = int(input("Введите координату Х точки C: "))
C_y = int(input("Введите координату Y точки C: "))
print() # Здесь и далее - для более аккуратного вывода

# Рассчитываем координаты векторов сторон
vec_AB = (B_x - A_x, B_y - A_y)
vec_BC = (C_x - B_x, C_y - B_y)
vec_CA = (A_x - C_x, A_y - C_y)

# Распаковываем координаты векторов в отдельные переменные
AB_x, AB_y = vec_AB
BC_x, BC_y = vec_BC
CA_x, CA_y = vec_CA

# Находим длины векторов
len_AB = math.sqrt(AB_x**2 + AB_y**2)
len_BC = math.sqrt(BC_x**2 + BC_y**2)
len_CA = math.sqrt(CA_x**2 + CA_y**2)

# Выводим длины сторон
print(f"Длина стороны АВ - {len_AB:6g}")
print(f"Длина стороны BC - {len_BC:6g}")
print(f"Длина стороны АC - {len_CA:6g}")
print()

# Проверяем, может ли существовать треугольник с такими длинами сторон
cond_AB = len_AB < len_BC + len_CA
cond_BC = len_BC < len_AB + len_CA
cond_CA = len_CA < len_AB + len_BC

# Завершаем программу в случае несуществования такого треугольника
if not (cond_AB and cond_BC and cond_CA):
    print("Такого треугольника не существует, сумма двух " \
           "сторон должна быть меньше третьей стороны.")
    sys.exit()

# Находим максимум среди длин сторон
max_length = max(len_AB, len_BC, len_CA)

# Записываем вектор наибольшей стороны и предшествующий ему в отдельные переменные.
if max_length == len_AB:
    vec_max_side = vec_AB
    vec_prev_side = vec_CA
    median_name = "CM"
elif max_length == len_BC:
    vec_max_side = vec_BC
    vec_prev_side = vec_AB
    median_name = "AM"
else:
    vec_max_side = vec_CA
    vec_prev_side = vec_BC
    median_name = "BM"

# Распаковываем координаты векторов в отдельные переменные
max_side_x, max_side_y = vec_max_side
prev_side_x, prev_side_y = vec_prev_side

# Выражаем вектор медианы как сумму половины вектора наибольшей стороны
vec_median = (prev_side_x + max_side_x/2, prev_side_y + max_side_y/2)

# Распаковываем координаты вектора медианы и находим его длину
median_x, median_y = vec_median
len_median = math.sqrt(median_x**2 + median_y**2)

print(f"Длина медианы {median_name} - {len_median:6g}")
print()

# Сравнивая скалярные произведения векторов сторон с нулем,
# выясняем, есть ли среди них перпендикулярные
angle_ABC_is_90 = AB_x*BC_x + AB_y*BC_y == 0
angle_BCA_is_90 = BC_x*CA_x + BC_y*CA_y == 0
angle_CAB_is_90 = CA_x*AB_x + CA_y*AB_y == 0

# Если хотя бы два этих вектора перпендикулярны, треугольник считаем прямоугольным
is_right_angled = angle_ABC_is_90 or angle_BCA_is_90 or angle_CAB_is_90

# Выясняем для вывода, какой именно угол является прямым
right_angle_name = angle_ABC_is_90*"ABC" + angle_BCA_is_90*"BCA" + angle_CAB_is_90*"CAB"

if is_right_angled:
    print(f"Треугольник является прямоугольным. Прямой угол - {right_angle_name}")
else:
    print("Треугольник не является прямоугольным")
print()

# Запрашиваем ввод координат точки, которрую необходимо
# проверить на нахождение внутри треугольника
print("Назовем точку, которую необходимо проверить, P.")
P_x = int(input("Введите координату X точки P: "))
P_y = int(input("Введите координату Y точки P: "))
print()

# Находим координаты векторов, ведущих из этой точки к вершинам треугольников
vec_PA = (A_x - P_x, A_y - P_y)
vec_PB = (B_x - P_x, B_y - P_y)
vec_PC = (C_x - P_x, C_y - P_y)

# Распаковываем координаты векторов в отдельные переменные
PA_x, PA_y = vec_PA
PB_x, PB_y = vec_PB
PC_x, PC_y = vec_PC

# Находим псевдоскалярные произведения вышеописанных векторов с векторами соответствующих сторон
psp_PA_AB = PA_x*AB_y - PA_y*AB_x
psp_PB_BC = PB_x*BC_y - PB_y*BC_x
psp_PC_CA = PC_x*CA_y - PC_y*CA_x

# Если одно из произведений равно нулю, точка лежит на границе треугольника
if psp_PA_AB == 0:
    print("Точка лежит на отрезке AB")
elif psp_PB_BC == 0:
    print("Точка лежит на отрезке ВС")
elif psp_PC_CA == 0:
    print("Точка лежит на отрезке AC")
else:
    # Сохраняем только знаки псевдоскалярных произведений
    sign_psp_PA_AB = math.copysign(1, psp_PA_AB)
    sign_psp_PB_BC = math.copysign(1, psp_PB_BC)   
    sign_psp_PC_CA = math.copysign(1, psp_PC_CA)

    # Если три произведения имеют один и тот же знак, точка лежит внутри треугольника
    is_inside = sign_psp_PA_AB == sign_psp_PB_BC == sign_psp_PC_CA

    # Расстояния до сторон легко вычисляются из псевдоскалярных произведений
    dist_P_AB = abs(psp_PA_AB) / len_AB
    dist_P_BC = abs(psp_PB_BC) / len_BC
    dist_P_CA = abs(psp_PC_CA) / len_CA

    min_dist = min(dist_P_AB, dist_P_BC, dist_P_CA)

    if is_inside:
        print("Точка лежит внутри треугольника. "\
             f"Минимальное расстояние до стороны - {min_dist:6g}")

    else:
        print("Точка лежит вне треугольника.")
