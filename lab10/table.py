def begin_table(*args):
	num_columns, column_width = args

	hor_line = "-" * ((column_width + 1) * num_columns + 1)
	table_row = "|" + f"{{:>{column_width}}}|" * num_columns

	print(hor_line)

	return (hor_line, table_row)

def add_row(table, *data):
	hor_line, table_row = table
	print(table_row.format(*data))
	print(hor_line)
