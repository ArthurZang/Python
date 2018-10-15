from flask import Flask, render_template
from flask import request
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)

@app.route('/')
def index():
    #return '<h1>Hello Flask!</h1>'
    return render_template('index.html')

@app.route('/hello')
def hello():
    user_agent = request.headers.get('Usr-Agent')
    return '<p>Your browser is %s</p>' %user_agent

@app.route('/greet',defaults={'name':'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name

user = {
    'username': 'Grey Li',
    'bio': 'A boy loves moives and music.',
}

movies = [
    {'name': 'My Neighour Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy','year':'1993'},
]

@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies)

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('submit')


if __name__ == '__main__':
    app.run()



