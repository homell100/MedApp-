TABLE_NAME_PATIENT = "patient"
TABLE_NAME_STAFF = "staff"
TABLE_NAME_ROOM = "room"
TABLE_NAME_BED = "bed"
TABLE_NAME_STAFF_PATIENT = "staff_patient"

TABLES_COLUMNS = {
	TABLE_NAME_ROOM: ["id", "floor", "number_room"],
	TABLE_NAME_PATIENT: ["id", "name", "surname", "entry_date", "exit_date", "id_bed"],
	TABLE_NAME_STAFF: ["id", "name", "surname", "position"],
	TABLE_NAME_BED: ["id", "id_room"],
	TABLE_NAME_STAFF_PATIENT: ["id_staff", "id_patient", "start_date", "end_date"]
}

TABLE_COLUMNS_NAMES_IGNORED_INSERTION = {
	TABLE_NAME_ROOM: ["id"],
	TABLE_NAME_PATIENT: ["id"],
	TABLE_NAME_STAFF: ["id"],
	TABLE_NAME_BED: ["id"]
}

LIST_TABLE_ACCEPT_DUPLICATES = [TABLE_NAME_BED]