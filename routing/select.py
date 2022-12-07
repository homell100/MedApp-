from flask import render_template, request, redirect, Blueprint
import crud_functions as cf
from psycopg2 import errors as err
from database_design import *
import os
from pathlib import Path
import database_design as dbd

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
	records = cf.get_records(table_name="staff")
	return render_template("select.html", col_names=dbd.TABLES_COLUMNS[dbd.TABLE_NAME_STAFF],
	 table_name=dbd.TABLE_NAME_STAFF, records=records)

@select_page.route("/select_patient")
def select_patient():
	records = cf.get_records(table_name="patient")
	return render_template("select.html", col_names=dbd.TABLES_COLUMNS[dbd.TABLE_NAME_PATIENT],
	 table_name=dbd.TABLE_NAME_PATIENT, records=records)

@select_page.route("/select_room")
def select_room():
	records = cf.get_records(table_name="room")
	return render_template("select.html", col_names=dbd.TABLES_COLUMNS[dbd.TABLE_NAME_ROOM],
	 table_name=dbd.TABLE_NAME_ROOM, records=records)

@select_page.route("/select_bed")
def select_bed():
	records = cf.get_records(table_name="bed")
	return render_template("select.html", col_names=dbd.TABLES_COLUMNS[dbd.TABLE_NAME_BED],
	 table_name=dbd.TABLE_NAME_BED, records=records)
