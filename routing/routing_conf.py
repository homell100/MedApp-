import database_design as dbd

ROUTING_CONF = {
	dbd.TABLE_NAME_STAFF:
		{"route_insert": "/insert_staff",
		"route_add": "/add_staff",
		"html_form": "add_staff.html"},
	dbd.TABLE_NAME_PATIENT:
		{"route_insert": "/insert_patient",
		"route_add": "/add_patient",
		"html_form": "add_patient.html"},
	dbd.TABLE_NAME_ROOM:
		{"route_insert": "/insert_room",
		"route_add": "/add_room",
		"html_form": "add_room.html"},
	dbd.TABLE_NAME_BED:
		{"route_insert": "/insert_bed",
		"route_add": "/add_bed",
		"html_form": "add_bed.html"},
	dbd.TABLE_NAME_STAFF_PATIENT:
		{"route_insert": "/insert_staff_patient",
		"route_add": "/add_staff_patient",
		"html_form": "add_staff_patient.html"}
}