from app import app
from flask import render_template, flash, redirect, url_for
from app.form import LoginForm
@app.route('/')
@app.route('/index')
def index():
	user = {'nickname':'LJG'}
	posts = [
		{
			'author' : {'nickname':'John'},
			'body' : 'Beautiful day in Portland!'
		},
		{
			'author':{'nickname':'Bell'},
			'body':'The Avengers movie was so cool!'
		}
	]
	return render_template("index.html",
		title = 'Home',
		user = user,
		posts = posts)
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
        title = 'Sign In',
        form = form)