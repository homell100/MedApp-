
#---------------------
#INSERT
#---------------------

QUERY_INSERT_STAFF = """
INSERT INTO staff(name, surname, position)
	VALUES ('{name}', '{surname}', '{position}')
"""

QUERY_INSERT_PATIENT = """
INSERT INTO patient(name, surname, entry_date, exit_date, id_bed)
	VALUES ('{name}', '{surname}', '{entry_date}', '{exit_date}', {id_bed})
"""