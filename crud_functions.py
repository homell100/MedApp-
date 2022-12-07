from aux_functions import make_connection
import queries as q
from decorators import adding_hypens, converting_none_to_null

#---------------------
#INSERT
#---------------------

def create_insert_query(table_name, **dict_col_value):
	list_col_names = []
	list_values = []
	for key, value in dict_col_value.items():
		list_col_names.append(key)
		list_values.append(value)
	string_col_names = q.COMMA_SEPARATOR.join(list_col_names)
	string_values = q.COMMA_SEPARATOR.join(list_values)

	query = ""
	query += q.TEMPLATE_QUERY_INSERT_TABLE.format(table=table_name, 
		list_col_names=string_col_names)
	query += q.TEMPLATE_QUERY_INSERT_VALUES.format(list_values=string_values)
	return query

@adding_hypens
@converting_none_to_null
def insert_query(table_name, **dict_col_value):
	conn = make_connection()
	with conn.cursor() as cur:
		query = create_insert_query(table_name, **dict_col_value)
		cur.execute(query)
	conn.commit()
	conn.close()

def create_check_duplicate_records_query(table_name, **kwarg):
	query = q.TEMPLATE_QUERY_CHECK_RECORDS_EXIST.format(table=table_name)
	query_where_parts = []
	for key, value in kwarg.items():
		if len(value):
			query_where_part = q.CLAUSE_WHERE_VALUE.format(column_name=key, value=value)
		else:
			query_where_part = q.CLAUSE_WHERE_NULL.format(column_name=key)
		query_where_parts.append(query_where_part)
	query += q.AND_SEPARATOR.join(query_where_parts)
	return query

@adding_hypens
def check_record(table_name, **kwarg):
	conn = make_connection()
	list_records = []
	with conn.cursor() as cur:
		query = create_check_duplicate_records_query(table_name, **kwarg)
		print(query)
		cur.execute(query)
		list_records = cur.fetchall()
	conn.close()
	return list_records

#---------------------
#SELECT
#---------------------

	
def get_records(table_name):
	conn = make_connection()
	list_records = []
	with conn.cursor() as cur:
		query = q.TEMPLATE_QUERY_SELECT.format(table=table_name)
		cur.execute(query)
		list_records = cur.fetchall()
	print(list_records)
	return list_records
