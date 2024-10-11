# Clyde 'Thluffy' Sinclair
# SoftDev
# October 2024

import os
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect

app = Flask(__name__)
secret = os.urandom(32)
app.secret_key = secret

@app.route('/', methods=['GET','POST'])
def redirection():
    return redirect('/login')

@app.route('/login', methods=['GET','POST'])
def disp_loginpage():
    loggedinquestion = 'You are not logged in'
    if 'username' in session:
        loggedinquestion = 'Logged in as: ' + session["username"]
        return render_template('/login', loggedin = loggedinquestion, html = "<br>")
        #return redirect('response')
    if request.method =='POST':
        session['username'] = request.form['username']
        return redirect('/response.html')
    print(session.get('username'))
    if session.get('username'):
        print("TRUEEEEEEEEEEE")
    htmlcode = '''
    <form action="/response.html">
      <input type="text" name="username">
      <input type="submit" name="sub1">
    </form>
    '''
    return render_template( 'login.html', loggedin=loggedinquestion, html = htmlcode)

@app.route("/response.html" , methods=['GET','POST'])
def authenticate():
    session['username'] = request.args.get('username')
    return render_template( 'response.html', username = request.args['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('login')#render_template('logout.html', logout = redirect('/login'))

if __name__ == "__main__":
    app.debug = True 
    app.run()
