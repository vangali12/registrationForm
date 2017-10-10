from flask import Flask, redirect, render_template, flash, request
import re

app = Flask(__name__)
app.secret_key = 'hushhush'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def display():
	return render_template('index.html')

@app.route('/addUser', methods=['POST'])
def addUser():
	status = True
	print("status true")
	if len(request.form['fName']) < 1:
		flash("Please enter a First Name")
		status = False
	if len(request.form['lName']) < 1:
		flash("Please enter a Last Name")
		status = False
	if len(request.form['email']) < 1:
		flash("Please enter an email address")
		status = False
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Please enter valid email address")
		status = False
	if len(request.form['password']) < 1:
		flash("Please enter a password")
		status = False
	elif len(request.form['password']) < 9:
		flash("Password should be at least 8 charcters")
		status = False
	elif (request.form['password'] != request.form['confirmPassword']):
		flash("Password and Confirm Password should match")
		status = False
	if len(request.form['confirmPassword']) < 1:
		flash("Please confirm your password")
		status = False
	if (re.search(r'\d', request.form['fName'])):
		flash("Please enter a valid First Name without numbers")
		status = False
	if (re.search(r'\d', request.form['lName'])):
		flash("Please enter a valid Last Name without numbers")
		status = False
	if status == False:
		return redirect('/')
	fName = request.form['fName']
	lName = request.form['lName']
	email = request.form['email']
	password = request.form['password']
	confirmPassword = request.form['confirmPassword']
	return redirect('/')

app.run(debug=True)