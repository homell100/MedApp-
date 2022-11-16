from flask import render_template, request, redirect, Blueprint
import crud_functions as cf
from psycopg2 import errors as err
import datetime
import error_messages as em
import database_design as dbd 

insert_page = Blueprint('insert_page', __name__, 
						template_folder='templates')

#---------------------
#INSERT
#---------------------

def insert(table_name):
	dict_values = {key:value for key, value in request.form.items() if key in dbd.TABLES_COLUMNS[table_name]}
	print(dict_values)
	if len(cf.check_record(table_name, **dict_values)):
		return False
	cf.insert_query(table_name, **dict_values)
	return True

#-------
#Staff
#-------
@insert_page.route("/add_staff")
def form_add_staff():
	return render_template("add_staff.html")

@insert_page.route("/insert_staff", methods=["GET", "POST"])
def insert_staff():
	if not insert(dbd.TABLE_NAME_STAFF):
		return render_template("add_staff.html", 
			error=em.ERROR_REPEATED_RECORD)
	return redirect("/home")


#-------
#Patient
#-------
@insert_page.route("/add_patient")
def form_add_patient():
	return render_template("add_patient.html")

@insert_page.route("/insert_patient", methods=["GET", "POST"])
def insert_patient():
	if not insert(dbd.TABLE_NAME_PATIENT):
		return render_template("add_patient.html", 
			error=em.ERROR_REPEATED_RECORD)
	return redirect("/home")


#-------
#Room
#-------
@insert_page.route("/add_room")
def form_add_room():
	return render_template("add_room.html")

@insert_page.route("/insert_room", methods=["GET", "POST"])
def insert_room():
	if not insert(dbd.TABLE_NAME_ROOM):
		return render_template("add_room.html", 
			error=em.ERROR_REPEATED_RECORD)
	return redirect("/home")
