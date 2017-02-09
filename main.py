#K.Koltermann
from flask import Flask, redirect, url_for
import database
import whateverYouNeed
import user
app = Flask(__name__)

@app.route('/homeguest')
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
            return render_template("homeuser.html",username)
            #logout button links to homeguest
        else:
            return redirect(url_for("badlogin"))

#TODO: K.KOLTERMANN: both login and search are in the same form, need to fix
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

@app.route('/noresultuser',searchString)
def noresultuser():
    return render_template("noresultuser.html",searchString)

@app.route('/noresultguest',searchString)
def noresultguest():
    return render_template("noresultguest.html",searchString)

@app.route('/createnewuser')
def login():
    return render_template("createnewuser.html")

@app.route('/badlogin')
def badlogin():
    return render_template("badlogin.html")
    #login link --> homeuser, which does the check again

#I'm sure there is a much easier way to to this
@app.route('/nightlifeuser',username)
def nightlifeu():
    return render_template("nightlifeu.html",username)

@app.route('/nightlifeguest')
def nightlifeg():
    return render_template("nightlifeg.html")

@app.route('/entertainmentuser',username)
def entertainmentu():
    return render_template("entertainmentu.html",username)

@app.route('/entertainmentguest')
def entertainmentg():
    return render_template("entertainmentg.html")

@app.route('/dininguser',username)
def entertainmentu():
    return render_template("diningu.html",username)

@app.route('/diningguest')
def entertainmentg():
    return render_template("diningg.html")
    
        

if __name__ == "__main__":
    app.run()
