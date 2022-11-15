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
#-------
#Staff
#-------
@insert_page.route("/add_staff")
def form_add_staff():
	return render_template("add_staff.html")

@insert_page.route("/insert_staff", methods=["GET", "POST"])
def insert_staff():
	name = request.form["name"]
	surname = request.form["surname"]
	position = request.form["position"]
	cf.insert_staff(name, surname, position)
	return redirect("/home")


#-------
#Patient
#-------
@insert_page.route("/add_patient")
def form_add_patient():
	return render_template("add_patient.html")

@insert_page.route("/insert_patient", methods=["GET", "POST"])
def insert_patient():
	name = request.form["name"]
	surname = request.form["surname"]
	entry_date = request.form["entry_date"]
	exit_date = request.form["exit_date"]
	id_bed = request.form["id_bed"]
	cf.insert_patient(name, surname, entry_date, exit_date, id_bed)
	return redirect("/home")

#-------
#Room
#-------
@insert_page.route("/add_room")
def form_add_room():
	return render_template("add_room.html")

@insert_page.route("/insert_room", methods=["GET", "POST"])
def insert_room():
	floor = request.form["floor"]
	room_number = request.form["room_number"]

	rooms = cf.check_record_room(floor, room_number)
	if len(rooms):
		return render_template("add_room.html", 
			error=em.ERROR_REPEATED_RECORD)

	cf.insert_room(floor, room_number)
	return redirect("/home")
