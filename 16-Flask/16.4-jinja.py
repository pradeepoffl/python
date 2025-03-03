''' 
Jinija template engine is handle by render_template 
There are multiple way to handle data source i.e data files in Jinija template engine one is below

{{   }} expressions to print output in html
{%  %} conditions, for loops
{#  #} this is for comments

## variable rules
## Dynamic urls


'''

from flask import Flask,render_template,request,redirect,url_for
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


## variable rules
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="Passed"
    else:
        res="Failed"
    return render_template('result.html',results=res)

@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="Passed"
    else:
        res="Failed" 
    exp={'score':score,'res':res} # expresion
    return render_template('successres.html',results=exp)


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',results=score)

@app.route('/submit',methods=['GET','POST'])
def submit():
    total_score=0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])

        total_score = (science+maths+datascience+c)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score))



# Execution start from here
if __name__ == '__main__':
    app.run(debug = True)

