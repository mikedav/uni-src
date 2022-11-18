"""
Подтверждение ввода
"""


cast_errmsg = "Проверьте введенные данные и повторите ввод."

# Валидатор - любое значение
def v_any(num):
	pass

# Валидатор - в диапазоне
def v_in_range(num, low, high, low_strict=False, high_strict=False):
	if (low_strict and (num <= low)) or (num < low):
		return f"Число должно быть больше {low:6g}"
	if (high_strict and (num >= high)) or (num > high):
		return f"Число должно быть меньше {high:6g}"

# Валидатор - положительное число
def v_is_positive(num):
	return v_in_range(num, 0, float("inf"), low_strict=True)

# Обработка ввода
# Принимает сообщение, тип, к которому надо привести,
# функцию-валидатор, аргументы для валидатора
def validate_input(msg, *v_args, cast_to=str, validator=v_any, **v_kwargs):
	rv = None
	while rv == None:
		try:
			rv = cast_to(input(msg))
			errmsg = validator(rv, *v_args, **v_kwargs)
			if errmsg:
				print(errmsg)
				rv = None
		except:
			print(cast_errmsg)
		
	return rv

# Запросить целое
def next_int(msg=""):
	return validate_input(msg, cast_to=int)

# Запросить дробное
def next_float(msg=""):
	return validate_input(msg, cast_to=float)

# Запросить натуральное
def next_natural(msg=""):
	return validate_input(msg, cast_to=int, validator=v_is_positive)

# Запросить дробное в диапазоне
def next_float_in_range(low, high, msg=""):
	return validate_input(msg, low, high, cast_to=float, validator=v_in_range)

# Запросить целое в диапазоне
def next_int_in_range(low, high, msg=""):
	return validate_input(msg, low, high, cast_to=int, validator=v_in_range)
