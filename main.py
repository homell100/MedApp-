from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.secret_key = "biiqw73_^¨PLAKV7tejas@~#2d"

@app.route("/")
def index():
	return render_template("home.html")

if __name__ == "__main__":
	app.run(host="127.0.0.1", port=8080, debug=True)
