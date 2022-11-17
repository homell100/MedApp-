TABLE_NAME_PATIENT = "patient"
TABLE_NAME_STAFF = "staff"
TABLE_NAME_ROOM = "room"
TABLE_NAME_STAFF_PATIENT = "staff_patient"

TABLES_COLUMNS = {
	TABLE_NAME_ROOM: ["floor", "number_room"],
	TABLE_NAME_PATIENT: ["name", "surname", "entry_date", "exit_date", "id_bed"],
	TABLE_NAME_STAFF: ["name", "surname", "position"],
	TABLE_NAME_STAFF_PATIENT: ["id_staff", "id_patient", "start_date", "end_date"]

}