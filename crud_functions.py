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
