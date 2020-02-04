from flask import Flask, redirect, url_for, render_template, request, session, send_file


app = Flask(__name__)


@app.route("/")
def home():
	return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		user = request.form["nm"]
		session["user"] = user
		return redirect(url_for("user", usr=user))
	else:
		return render_template("login.html")


@app.route("/file", methods=["GET"])
def generate_pdf():
	return render_template("pdf.html")


@app.route("/file_download")
def file_download():
	return send_file('/Users/rob/Documents/GitHub/BloodAnalysis/Models/test.txt')


@app.route("/<usr>")
def user(usr):
	return f"<h1>{usr}</h1>"


@app.route("/params")
def params():

	arg1 = request.args['arg1']
	arg2 = request.args['arg2']

	return ""


if __name__ == "__main__":
	app.run()