
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
QUERY_INSERT_PATIENT = """
INSERT INTO patient(name, surname, entry_date, exit_date, id_bed)
	VALUES ({name}, {surname}, {entry_date}, {exit_date}, {id_bed})
"""

#-------
#Room
#-------
QUERY_INSERT_ROOM = """
INSERT INTO room(floor, number_room)
	VALUES ({floor}, {number_room})
"""

QUERY_CHECK_RECORD_EXISTS_ROOM = """
SELECT id
FROM room
WHERE floor={floor} AND number_room={number_room}
"""