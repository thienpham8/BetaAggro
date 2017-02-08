#K.Koltermann
from flask import Flask, redirect, url_for
import database
import whateverYouNeed
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

@app.route('/badlogin')
def badlogin():
    return render_template("badlogin")
    #login link --> homeuser, which does the check again

#I'm sure there is a much easier way to to this
@app.route('/nightlifeuser',username)
def nightlifeu():
    return render_template("nightlifeu.html",username"

@app.route('/nightlifeguest')
def nightlifeg():
    return render_template("nightlifeg.html")
    
        

if __name__ == "__main__":
    app.run()
