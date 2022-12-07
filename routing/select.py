from flask import render_template, request, redirect, Blueprint
import crud_functions as cf
from psycopg2 import errors as err
from database_design import *
import os
from pathlib import Path

template_folder = Path('templates')
subfolder_templates = "select" 
template_folder_full_path = os.getcwd() / template_folder / subfolder_templates

select_page = Blueprint('select_page', __name__, 
						template_folder=template_folder_full_path)

#---------------------
#SELECT
#---------------------

@select_page.route("/select_staff")
def select_staff():
	staffs = cf.get_staff()
	return render_template("select.html", table_name="staff", records=staffs)

@select_page.route("/select_patient")
def select_patient():
	patients = cf.get_patient()
	return render_template("select.html", table_name="patient", records=patients)

@select_page.route("/select_room")
def select_room():
	rooms = cf.get_room()
	return render_template("select.html", table_name="room", records=rooms)

@select_page.route("/select_bed")
def select_bed():
	beds = cf.get_bed()
	return render_template("select.html", table_name="bed", records=beds)
