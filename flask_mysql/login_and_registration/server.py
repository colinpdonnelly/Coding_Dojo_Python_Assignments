from flask import Flask, request, redirect, render_template, session, flash
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'hello_world'
mysql = MySQLConnector(app, 'login')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    pconfirm = request.form['pconfirm']

    if len(first_name) < 2 or len(last_name) < 2:
        flash('Not enough characters! Try again!', 'error')
    if not NAME_REGEX.match(first_name) or not NAME_REGEX.match(last_name):
        flash('First and last name must only include letters.', 'error')
    if not EMAIL_REGEX.match(email):
        flash('Invalid Email Address!', 'error')
    if len(password) < 8:
        flash('Password must be at least 8 characters!', 'error')
    if password != pconfirm:
        flash('Passwords must match!', 'error')
    else:
        query = 'INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, now(), now())'
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'pconfirm': pconfirm
        }
        mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
