import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set in Heroku (Settings->Config Vars).  
                                     #To run locally, set in env.sh and include that file in gitignore so the secret key is not made public.

@app.route('/',methods=['GET','POST'])
def renderMain():
    if 'firstName' in request.form:
        session["firstName"]=request.form['firstName']
        session["lastName"]=request.form['lastName']
    return render_template('name.html')

@app.route('/quiz')
def renderQuiz():
    if 'num_acids' in request.form:
        session["q1"]=request.form['num_acids']
    if 'thym=acid?' in request.form:
        session["q2"]=request.form['thym=acid?']
    if 'uran=acid?' in request.form:
        session["q3"]=request.form['uran=acid?']
    return render_template('quiz.html')

#@app.route('/startOver')
#def startOver():
#    session.clear() #clears variable values and creates a new session
#    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/results',methods=['GET','POST'])
def renderPage2():
    session["firstName"]=request.form['firstName']
    session["lastName"]=request.form['lastName']
    return render_template('page2.html')
    
if __name__=="__main__":
    app.run(debug=True)