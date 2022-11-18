import integral as il
import validate as vi
from table import begin_table, add_row

def main(subject, real_a_der):
    sections_num1 = vi.next_natural("Введите первое количество участков разбиения: ")
    sections_num2 = vi.next_natural("Введите второе количество участков разбиения: ")
    interval_start = vi.next_float("Введите начало интервала: ")
    interval_end = vi.next_float_in_range(interval_start, float("inf"), "Введите конечную точку интервала: ")
    eps = vi.next_float("Введите необходимую точность: ")

    # Для устранения ошибок в представлении чисел с плавающей запятой
    eps_zero = 1e-5
    max_iter = 2**20

    # Считаем интеграл аналитически
    integral_real = il.integral_real(interval_start, interval_end, real_a_der)

    # Для удобства вынесем вычисление интегралов нужными методами в функции с короткими названиями
    def lc_integral(sections_num):
        return il.integral_digital(interval_start, interval_end, sections_num, subject, il.m_left_column)

    def te_integral(sections_num):
        return il.integral_digital(interval_start, interval_end, sections_num, subject, il.m_trapezia)
    
    # Вынесем вычисление относительной и абсолютной погрешности в отдельные функции
    def get_abs_err(integral_value):
        abs_err = abs(integral_real - integral_value)
        return abs_err if abs(abs_err) > eps_zero else 0.

    def get_rel_err(abs_err):
        if integral_real != 0.:
            return abs_err/integral_real
        else:
            return "Не вычислено"

    # Считаем нужные интегралы, абсолютные и относительное погрешности
    int_values = (lc_integral(sections_num1), lc_integral(sections_num2), te_integral(sections_num1), te_integral(sections_num2))

    if None in int_values:
        print("Функция не интегрируема на отрезке")
        quit()

    abs_err = tuple(map(get_abs_err, int_values))
    rel_err = tuple(map(get_rel_err, abs_err))

    # Выбираем, какой метод более точен, а какой мы будем испытывать
    best_method_index = (abs_err.index(min(abs_err))) // 2
    tested_method = (te_integral, lc_integral)[best_method_index]

    # Ищем необходимое число разбиений
    sections_num = 1

    left = tested_method(sections_num)
    right = tested_method(sections_num * 2)
    delta = abs(right - left)

    while delta > eps and sections_num < max_iter:
        sections_num *= 2
        left, right = right, tested_method(sections_num * 2)
        delta = abs(right - left)


    # Печатаем таблицу
    table = begin_table(3, 25)
    add_row(table, "", f"N1={sections_num1}", f"N2={sections_num2}")
    add_row(table, "Метод левых прямоуг.", int_values[0], int_values[1])
    add_row(table, "Метод 3/8.", int_values[2], int_values[3])
    add_row(table, "Аналит. пол. зн.", integral_real, "")
    add_row(table, "Абс. погр. метода 1", abs_err[0], abs_err[1])
    add_row(table, "Абс. погр. метода 2", abs_err[2], abs_err[3])
    add_row(table, "Отн. погр. метода 1", rel_err[0], rel_err[1])
    add_row(table, "Отн. погр. метода 2", rel_err[2], rel_err[3])

    print(f"Более быстрым оказался метод {('левых прямоугольников', 'трех восьмых')[best_method_index]}")
    if sections_num == max_iter:
        print("Не дается вычислить интеграл с заданной точностью")
        print(f"При разбиении на {sections_num} участков достигнута точность {delta:6g}")
    else:
        print(f"Для менее точного метода необходимо {sections_num} для достижения указанной точности")
    


