from flask import render_template, request, redirect, Blueprint
import crud_functions as cf
from psycopg2 import errors as err
import error_messages as em
import database_design as dbd 
import routing.routing_conf as rc

insert_page = Blueprint('insert_page', __name__, 
						template_folder='templates')

def insert(table_name):
	succed = True
	error_message = ""

	dict_values = {key:value for key, value in request.form.items()\
	if key in dbd.TABLES_COLUMNS[table_name]}
	print(dict_values)
	if (table_name not in dbd.LIST_TABLE_ACCEPT_DUPLICATES) &\
	len(cf.check_record(table_name, **dict_values)):
		succed = False
		error_message = em.ERROR_REPEATED_RECORD
	try:
		cf.insert_query(table_name, **dict_values)
	except err.ForeignKeyViolation as e:
		succed = False
		error_message = em.ERROR_WRONG_FOREING_KEY + str(e)
	return succed, error_message

def attempt_insert(table_name):
	succed, error_message = insert(table_name)
	if not succed:
		return render_template(rc.ROUTING_CONF[table_name]["html_form"], 
			error=error_message)
	return redirect("/home")

#-------
#Staff
#-------
table_staff = dbd.TABLE_NAME_STAFF
@insert_page.route(rc.ROUTING_CONF[table_staff]["route_add"])
def form_add_staff():
	return render_template(rc.ROUTING_CONF[table_staff]["html_form"])

@insert_page.route(rc.ROUTING_CONF[table_staff]["route_insert"], methods=["GET", "POST"])
def insert_staff():
	return attempt_insert(table_staff)

#-------
#Patient
#-------
table_patient = dbd.TABLE_NAME_STAFF
@insert_page.route(rc.ROUTING_CONF[table_staff]["route_add"])
def form_add_patient():
	return render_template(rc.ROUTING_CONF[table_patient]["html_form"])

@insert_page.route(rc.ROUTING_CONF[table_patient]["route_insert"], methods=["GET", "POST"])
def insert_patient():
	return attempt_insert(table_patient)


#-------
#Bed
#-------
table_room = dbd.TABLE_NAME_ROOM
@insert_page.route(rc.ROUTING_CONF[table_room]["route_add"])
def form_add_room():
	return render_template(rc.ROUTING_CONF[table_room]["html_form"])

@insert_page.route(rc.ROUTING_CONF[table_room]["route_insert"], methods=["GET", "POST"])
def insert_room():
	return attempt_insert(table_room)

#-------
#Room
#-------
table_bed = dbd.TABLE_NAME_BED
@insert_page.route(rc.ROUTING_CONF[table_bed]["route_add"])
def form_add_bed():
	return render_template(rc.ROUTING_CONF[table_bed]["html_form"])

@insert_page.route(rc.ROUTING_CONF[table_bed]["route_insert"], methods=["GET", "POST"])
def insert_bed():
	return attempt_insert(table_bed)

#-------
#Staff Patient
#-------
table_staff_patient = dbd.TABLE_NAME_STAFF_PATIENT
@insert_page.route(rc.ROUTING_CONF[table_staff_patient]["route_add"])
def form_add_staff_patient():
	return render_template(rc.ROUTING_CONF[table_staff_patient]["html_form"])

@insert_page.route(rc.ROUTING_CONF[table_staff_patient]["route_insert"], methods=["GET", "POST"])
def insert_staff_patient():
	return attempt_insert(table_staff_patient)
