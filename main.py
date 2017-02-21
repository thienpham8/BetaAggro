#K.Koltermann
from flask import Flask, redirect, url_for, flash, request, Response, render_template, send_from_directory
import business
import admin
import const
import dbConnector
import user
#app = Flask(__name__)
app = Flask(__name__, static_url_path='')


@app.route('/resources/<path:path>')
def send_js(path):
    return send_from_directory('resources', path)

@app.route('/')
def homeguest():
    return render_template("homeguest.html")
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
            return render_template("homeuser.html",username)
            #logout button links to homeguest
        else:
            flash('Login failed', 'Error')
            return redirect(url_for("badlogin"))

#TODO: K.KOLTERMANN: both login and search are in the same form, need to fix
#2/12/17: K.Koltermann: actually its okay
@app.route('/searchuser',methods = ["POST"])
def searchu():
    if request.method == 'POST':
        searchString = request.form['search']
        #NEED TO TALK ABOUT THIS: we should create a user object which is inherited
        data = db.search(searchString,self.user.zipcode)
        #have data return false, null, whatever if nothing found
        if data:
            return render_template("searchuser.html",data)
        else:
            redirect(url_for("noresultuser",searchString))
            
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


@app.route('/aboutus')
def aboutUs():
    return render_template("AboutUs.html")

@app.errorhandler(404)
def bad_url(exc):
    return Response('<h3>Not found</h3'),404

@app.errorhandler(403)
def forbidden(exc):
    return Response('<h3>Forbidden<h3>'),403

@app.route('/noresultuser')
def noresultuser():
    return render_template("noresultuser.html",searchString)

@app.route('/noresultguest')
def noresultguest():
    return render_template("noresultguest.html",searchString)

@app.route('/createnewuser')
def login():
    return render_template("Register.html")

@app.route('/badlogin')
def badlogin():
    return render_template("badlogin.html")
    #login link --> homeuser, which does the check again

#I'm sure there is a much easier way to to this
@app.route('/nightlifeuser')
def nightlifeu():
    return render_template("nightlifeu.html",username)

@app.route('/nightlifeguest')
def nightlifeg():
    return render_template("nightlifreg.html")

@app.route('/entertainmentuser')
def entertainmentu():
    return render_template("entertainmentu.html",username)

@app.route('/entertainmentguest')
def entertainmentg():
    return render_template("entertainmentg.html")

@app.route('/dininguser')
def diningu():
    return render_template("diningu.html",username)

@app.route('/diningguest')
def diningg():
    return render_template("diningg.html")
    
        

if __name__ == "__main__":
    app.run() 
