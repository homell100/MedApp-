
CHECK_RECORDS_EXIT_PARAM = "id"
COMMA_SEPARATOR = ","

#---------------------
#INSERT
#---------------------
#-------
#Staff
#-------
QUERY_INSERT_STAFF = """
INSERT INTO staff(name, surname, position)
	VALUES ({name}, {surname}, {position})
"""

#-------
#Patient
#-------

TEMPLATE_QUERY_INSERT_TABLE = """
INSERT INTO {table} ({list_col_names})
"""

TEMPLATE_QUERY_INSERT_VALUES = """
VALUES({list_values})
"""

QUERY_INSERT_PATIENT = """
INSERT INTO patient(name, surname, entry_date, exit_date, id_bed)
	VALUES ({name}, {surname}, {entry_date}, {exit_date}, {id_bed})
"""

TEMPLATE_QUERY_CHECK_RECORDS_EXIST = """
SELECT
""" + CHECK_RECORDS_EXIT_PARAM + """
FROM
	{table}
WHERE 
"""

CLAUSE_WHERE_VALUE = """
{column_name} = {value}
"""

CLAUSE_WHERE_NULL = """
{column_name} IS NULL
"""

AND_SEPARATOR = " AND "

#-------
#Room
#-------
QUERY_INSERT_ROOM = """
INSERT INTO room(floor, number_room)
	VALUES ({floor}, {number_room})
"""