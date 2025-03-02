## BASIC Flask app Skeleton with HTML templates 
## Understanding Get Method:- Fetching data from the server
## Understanding Post Method:- Sending data to the server more secure ex..login details 

from flask import Flask,render_template,request
'''
1. It creates an instance of the Flask class,
which will be your WSGI (web server gateway interface) application.
2. render_template will redirect to that particular HTML file with templates folder.
'''

## WSGI application ## Requests and response
app = Flask(__name__)

@app.route('/')

def Welcome():
    return '''<html><H1> Welcome to my Flask application!</H1> 
    <H2>We build amazing ML models here!!</H2></html>'''

@app.route('/index',methods = ['GET']) # Default method is Get 

def Index():
    return render_template("index.html")

@app.route('/aboutus')

def AboutUs():
    return render_template("aboutus.html")

@app.route('/form',methods=['GET','POST'])

def form():
    if request.method == 'POST':
        name=request.form['name']
        return f'Hello {name} !! '
    return render_template("form.html")

# Execution start from here
if __name__ == '__main__':
    app.run(debug = True)

