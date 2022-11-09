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
