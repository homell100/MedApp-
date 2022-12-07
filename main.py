from flask import Flask, render_template, redirect, request

from routing.insert import insert_page
from routing.select import select_page

app = Flask(__name__)
app.secret_key = "biiqw73_^¨PLAKV7tejas@~#2d"

app.register_blueprint(insert_page)
app.register_blueprint(select_page)


@app.route("/home")
@app.route("/")
def index():
	return render_template("home.html")

if __name__ == "__main__":
	app.run(host="127.0.0.1", port=8080, debug=True)
