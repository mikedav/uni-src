"""
Печать таблицы
"""

# Начинает печать таблицы с заданными парметрами
# Возвращает кортеж строк для ее продолжения
def begin_table(*args):
	num_columns, column_width = args

	hor_line = "-" * ((column_width + 1) * num_columns + 1)
	table_row = "|" + f"{{:>{column_width}}}|" * num_columns

	print(hor_line)

	return (hor_line, table_row)

# Форматирует входные данные, если они имеют числовой тип
def format_if_needed(data):
	if type(data) == int or type(data) == float:
		return f"{data:6g}"
	return data

# Печатает очередную строку таблицы
def add_row(table, *data):
	hor_line, table_row = table
	print(table_row.format(*tuple(map(format_if_needed, data))))
	print(hor_line)
