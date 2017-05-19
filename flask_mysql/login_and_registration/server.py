from flask import Flask, request, redirect, render_template, session, flash
import re
import md5
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'hello_world'
mysql = MySQLConnector(app, 'login')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/wall')
def wall():
    if 'user' not in session:
        return redirect('/')
    return render_template('wall.html')


@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    pconfirm = md5.new(request.form['pconfirm']).hexdigest()

    if len(first_name) < 2 or len(last_name) < 2:
        flash('Not enough characters! Try again!', 'error')
    if not NAME_REGEX.match(first_name) or not NAME_REGEX.match(last_name):
        flash('First and last name must only include letters.', 'error')
    if not EMAIL_REGEX.match(email):
        flash('Invalid Email Address!', 'error')
    # if email != user[0]['email']:
    #     flash('Incorrect email!')
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


@app.route('/login', methods=['POST'])
def attempt():
    email = request.form['email']
    password = request.form['password']

    if len(email) < 1 or len(password) < 1:
        flash("Please enter both fields", 'error')
        flash("Email or password is incorrect. Please try again.", 'error')
    return redirect('/')


@app.route('/login', methods=["POST"])
def login():
    password = md5.new(request.form['password']).hexdigest()
    email = request.form['email']
    # my_password = request.form['password']
    user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
    query_data = {
        'email': email
    }
    user = mysql.query_db(user_query, query_data)

    if len(user) != 0:
        if password == user[0]['password']:
            session['user'] = {
                'id': user[0]['id'],
                'first': user[0]['first_name'],
                'last': user[0]['last_name']

            }
            # flash('You have successfully logged in', 'success')
            return redirect('/wall')
        else:
            flash('Incorrect password try again!', 'error')
            return redirect('/')
            # return render_template('login.html')
    return render_template('login.html')


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')


app.run(debug=True)
