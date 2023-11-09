table_name = "product"
column_list = [
    ("col1_name", "col1_type"),
    ("col2_name", "col2_type"),
    ("col3_name", "col3_type"),
]


column_strings = [f'{col_name} {col_type}' for col_name, col_type in column_list]
columns_query_string = ', '.join(column_strings)

query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_query_string})"

print(query)