from flask import *
from society import addData,loginvalidation,edit


app = Flask(__name__)



@app.route("/")
def login():	  
	return render_template("login.html")


@app.route("/signup")
def signup():
	return render_template("signup.html")

@app.route("/home")
def home():
	return render_template("home.html")



@app.route("/addData",methods=["GET","POST"])
def sign_up():
	Id=request.form["Id"]
	First=request.form["First"]
	Last=request.form["Last"]
	Email=request.form["Email"]
	Username=request.form["Username"]
	Password=request.form["Password"]

	t=(Id,First,Last,Email,Username,Password)
	addData(t)
	return render_template("login.html")


@app.route("/loginvalidation",methods=["GET","POST"])
def login_validation():
	Username = request.form.get("Username")
	Password = request.form.get("Password")

	a = (Username,Password)
	el = loginvalidation(a)

	if len(el)>0:
		return render_template("home.html",users="el")
	else:
		error = "Invalid Uername anad Password"
		return render_template("login.html",users="el",error = error)


@app.route("/logout")
def logout():
	return render_template("login.html")
if __name__ == "__main__":
	app.run(debug=True)
