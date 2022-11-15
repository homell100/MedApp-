from aux_functions import make_connection
import queries as q
from decorators import adding_hypens_to_args

#---------------------
#INSERT
#---------------------
@adding_hypens_to_args
def insert_staff(name, surname, position):
	conn = make_connection()
	with conn.cursor() as cur:
		query = q.QUERY_INSERT_STAFF.format(name=name,
												surname=surname,
												position=position)
		cur.execute(query)
	conn.commit()
	conn.close()

@adding_hypens_to_args
def insert_patient(name, surname, entry_date, exit_date, id_bed):
	conn = make_connection()
	with conn.cursor() as cur:
		query = q.QUERY_INSERT_PATIENT.format(name=name,
												surname=surname,
												entry_date=entry_date,
												exit_date=exit_date,
												id_bed=id_bed)
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

	
