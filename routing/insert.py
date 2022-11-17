from flask import render_template, request, redirect, Blueprint
import crud_functions as cf
from psycopg2 import errors as err
import error_messages as em
import database_design as dbd 

insert_page = Blueprint('insert_page', __name__, 
						template_folder='templates')

#---------------------
#INSERT
#---------------------
def insert(table_name):
	succed = True
	error_message = ""

	dict_values = {key:value for key, value in request.form.items() if key in dbd.TABLES_COLUMNS[table_name]}
	print(dict_values)
	if len(cf.check_record(table_name, **dict_values)):
		succed = False
		error_message = em.ERROR_REPEATED_RECORD
	try:
		cf.insert_query(table_name, **dict_values)
	except err.ForeignKeyViolation as e:
		succed = False
		error_message = em.ERROR_WRONG_FOREING_KEY + str(e)
	return succed, error_message

#-------
#Staff
#-------
@insert_page.route("/add_staff")
def form_add_staff():
	return render_template("add_staff.html")

@insert_page.route("/insert_staff", methods=["GET", "POST"])
def insert_staff():
	succed, error_message = insert(dbd.TABLE_NAME_STAFF)
	if not succed:
		return render_template("add_staff.html", 
			error=error_message)
	return redirect("/home")

#-------
#Patient
#-------
@insert_page.route("/add_patient")
def form_add_patient():
	return render_template("add_patient.html")

@insert_page.route("/insert_patient", methods=["GET", "POST"])
def insert_patient():
	succed, error_message = insert(dbd.TABLE_NAME_PATIENT)
	if not succed:
		return render_template("add_patient.html", 
			error=error_message)
	return redirect("/home")

#-------
#Room
#-------
@insert_page.route("/add_room")
def form_add_room():
	return render_template("add_room.html")

@insert_page.route("/insert_room", methods=["GET", "POST"])
def insert_room():
	succed, error_message = insert(dbd.TABLE_NAME_ROOM)
	if not succed:
		return render_template("add_room.html", 
			error=error_message)
	return redirect("/home")

#-------
#Staff Patient
#-------
@insert_page.route("/add_staff_patient")
def form_add_staff_patient():
	return render_template("add_staff_patient.html")

@insert_page.route("/insert_staff_patient", methods=["GET", "POST"])
def insert_staff_patient():
	succed, error_message = insert(dbd.TABLE_NAME_STAFF_PATIENT)
	if not succed:
		return render_template("add_staff_patient.html", 
			error=error_message)
	return redirect("/home")
