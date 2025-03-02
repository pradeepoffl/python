## BASIC Flask app Skeleton

from flask import Flask 
'''
It creates an instance of the Flask class,
which will be your WSGI (web server gateway interface) application.

'''

## WSGI application ## Requests and response
app = Flask(__name__)

@app.route('/')

def Welcome():
    return " Welcome to my Flask application! We build amazing ML models here!!"

@app.route('/index')

def Index():
    return " Welcome to Index page! We build amazing ML models here!!"

# Execution start from here
if __name__ == '__main__':
    app.run(debug = True)

