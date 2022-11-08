from aux_functions import make_connection
import queries as q

#---------------------
#INSERT
#---------------------
def insert_staff(name, surname, position):
	conn = make_connection()
	with conn.cursor() as cur:
		cur.execute(q.QUERY_INSERT_STAFF.format(name = name,
												 surname = surname,
												 position = position))
	conn.commit()
	conn.close()

def insert_patient(name, surname, entry_date, exit_date, id_bed):
	conn = make_connection()
	with conn.cursor() as cur:
		cur.execute(q.QUERY_INSERT_PATIENT.format(name = name,
													 surname = surname,
													 entry_date=entry_date,
													 exit_date=exit_date,
													 id_bed=id_bed)
		)
	conn.commit()
	conn.close()
