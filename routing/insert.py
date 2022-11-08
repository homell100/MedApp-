from flask import render_template, request, redirect, Blueprint
import crud_functions as cf
from psycopg2 import errors as err
import datetime

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
	# De cualquier modo, y si todo fue bien, redireccionar
	return redirect("/home")
