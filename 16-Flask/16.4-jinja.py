''' 
Jinija template engine is handle by render_template
{{   }} expressions to print output in html
{%  %} conditions, for loops
{#  #} this is for comments

## variable rules
## Dynamic urls


'''

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

def submit():
    if request.method == 'POST':
        name=request.form['name']
        return f'Hello {name} !! '
    return render_template("form.html")


## variable rules
@app.route('/success/<int:score>')
def success(score):
    return f'Congratulations, you have scored {str(score)}'

# Execution start from here
if __name__ == '__main__':
    app.run(debug = True)

