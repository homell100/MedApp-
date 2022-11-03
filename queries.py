
#---------------------
#INSERT
#---------------------

QUERY_INSERT_STAFF = """
INSERT INTO staff(name, surname, position)
	VALUES ('{name}', '{surname}', '{position}')
"""