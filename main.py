#K.Koltermann
from flask import Flask, redirect, url_for, flash, request, Response, render_template, send_from_directory
import business
import admin
import user
import const
import dbConnector
import yelp
import user
import flask_login
import sys

#app = Flask(__name__)
app = Flask(__name__, static_url_path="")
app.secret_key = "It's a secret, I'm serial!"
loginManager = flask_login.LoginManager()
loginManager.init_app(app)

# Smith: This will allow our pages to access betaaggro/resources folder for images
@app.route('/resources/<path:path>')
def send_js(path):
	return send_from_directory('resources', path)
# ------------------------------------------------------------------------------------ #


@loginManager.user_loader
def load_user(user_id):
	return user.User.get(user_id)


@app.route('/')
@app.route("/home")
def homeguest():

	err = request.args.get("error", "")
	
	return render_template("home.html", error=err)
	
	#on the homeguest.html file, form action = route method = name, for buttons
	#create new user button is outside <form></form> and links to new user page

	
@app.route('/homeuser',methods = ["POST"])
def homeuser():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		accept = db.checkUserPassword(username,password)
		if accept:
			flash('You are now logged in.', 'success')
			return render_template("home.html",username)
			#logout button links to homeguest
		else:
			flash('Login failed', 'Error')
			return redirect(url_for("badlogin"))

#TODO: K.KOLTERMANN: both login and search are in the same form, need to fix
#2/12/17: K.Koltermann: actually its okay
@app.route('/searchuser', methods = ["POST", "GET"])
def searchu():
	if request.method == 'POST':
		criteria = ("name", request.form['searchline'])
		y = yelp.YelpAPI()
		connection = dbConnector.Connector(verbose=False)
		
		data = connection.select(criteria, limit=10)
		
		if len(data) < 10:
			y.search(criteria[1], limit=10, addToDB=True, verbose=False)
		connection = dbConnector.Connector(verbose=False)
		data = connection.select(criteria, limit=10)
		
		if data:
			return render_template("search.html", found = True, response = data)
		else:
			return render_template("search.html", found = False, response = "Business Not Found")
			
	else:
		return render_template("home.html")
			
			
@app.route('/login', methods= ["POST", "GET"])
def login():

	if request.method == "GET":
		return render_template("Login.html")
	
	if request.method == "POST":
	
		usr = user.User()
		success = usr.login(request.form)
		
		if success:
			flask_login.login_user(usr)
			return redirect("/")	
		
		else:
			return redirect("/?error=Bad username/password.")
		
@app.route("/logout")
def logout():

	flask_login.logout_user()
	return redirect("/")
	
@app.route("/register", methods=["POST", "GET"])
def register():

	if request.method == "GET":
	
		return render_template("Register.html")
	
	if request.method == "POST":
	
		# try:
		dic = request.form
		print "form data : ", dic
		usr = user.User()
		success = usr.register(dic)
		if success:
			flask_login.login_user(usr)
			flash("Registration successfull. Welcome, {}".format(usr.firstname))
			print "registration success"
			return redirect("/")
		else:
			print "registration failure."
			return redirect("/?error=User already exists.")
		# except:
			# flash("Registration error.")
			# print "registration fail"
			# print sys.exc_info()[0]
			# print sys.exc_info()[1]
			# print sys.exc_info()[2]
			# return redirect("/")
			
@app.route('/aboutus')
def aboutUs():
	return render_template("AboutUs.html")

@app.route('/contactus')
def contactUs():
	return render_template("contactus.html")

@app.route('/dining')
def dining():
	return render_template("Dining.html")
	
@app.route('/entertainment')
def entertainment():
	return render_template("Entertainment.html")

@app.route('/nightlife')
def nightlife():
	return render_template("Nightlife.html")

@app.route('/porpoise')
def porpoise():
	return render_template("porpoise.html")
	
	
	
# ---- #	
					
@app.route('/searchguest',methods = ["POST"])
def searchg():
	if request.method == 'POST':
		searchString = request.form['search']
		zipcode = -1 #no zipcode since guest
		data = db.search(searchString,zipcode)
		if data:
			return render_template("searchguest.html",data)
		else:
			redirect(url_for("noresultguest",searchString))

@app.route('/usercreated',methods = ['POST','GET'])
def usercreated():
	if request.method == 'POST':
		result = request.form
		db.createUser(result)
		return render_template("usercreated.html",result)

@app.route('/userprofile',methods = ['POST','GET'])
def userprofile():
	if request.method == 'POST':
		result = request.form
		db.updateUser(result)
		return render_template("homeuser.html")

@app.errorhandler(404)
def bad_url(exc):
	return Response('<h3>Not found</h3'),404

@app.errorhandler(403)
def forbidden(exc):
	return Response('<h3>Forbidden<h3>'),403

@app.route('/noresultuser')
def noresultuser():
	return render_template("noresultuser.html")

@app.route('/noresultguest')
def noresultguest():
	return render_template("noresultguest.html")

@app.route('/badlogin')
def badlogin():
	return render_template("badlogin.html")
	#login link --> homeuser, which does the check again

#I'm sure there is a much easier way to to this
@app.route('/nightlifeuser')
def nightlifeu():
	return render_template("nightlifeu.html")

@app.route('/nightlifeguest')
def nightlifeg():
	return render_template("nightlifreg.html")

@app.route('/entertainmentuser')
def entertainmentu():
	return render_template("entertainmentu.html")

@app.route('/entertainmentguest')
def entertainmentg():
	return render_template("entertainmentg.html")

@app.route('/dininguser')
def diningu():
	return render_template("diningu.html")

@app.route('/diningguest')
def diningg():
	return render_template("diningg.html")
	
		

if __name__ == "__main__":
	app.run() 
