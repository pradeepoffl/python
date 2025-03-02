## BASIC Flask app Skeleton with HTML templates

from flask import Flask,render_template
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

@app.route('/index')

def Index():
    return render_template("index.html")

@app.route('/aboutus')

def AboutUs():
    return render_template("aboutus.html")

# Execution start from here
if __name__ == '__main__':
    app.run(debug = True)

