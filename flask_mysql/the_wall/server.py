from flask import Flask, request, redirect, render_template, session, flash
import re
import md5
from mysqlconnection import MySQLConnector
import os
import binascii
app = Flask(__name__)
app.secret_key = 'i_love_donuts'
mysql = MySQLConnector(app, 'wall')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/register', methods=["POST"])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    pconfirm = request.form['pconfirm']
    salt = binascii.b2a_hex(os.urandom(15))
    hashed_pw = md5.new(password + salt).hexdigest()
    boo = True

    if len(first_name) < 2 or len(last_name) < 2:
        flash('Not enough characters! Try again!', 'error')
        boo = False
    if not NAME_REGEX.match(first_name) or not NAME_REGEX.match(last_name):
        flash('First and last name must only include letters.', 'error')
        boo = False
    if not EMAIL_REGEX.match(email):
        flash('Invalid Email Address!', 'error')
        boo = False
    if len(password) < 8:
        flash('Password must be at least 8 characters!', 'error')
        boo = False
    if password != pconfirm:
        flash('Passwords must match!', 'error')
        boo = False
    if boo is True:
        insert_query = "INSERT INTO users(first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :hashed_pw, :salt, now(), now())"
        query_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'hashed_pw': hashed_pw,
            'salt': salt
        }
        mysql.query_db(insert_query, query_data)
        return redirect('/')

    return redirect('/')


@app.route('/wall')
def wall():
    friends = mysql.query_db(
        "SELECT messages.id, user_id, message, DATE_FORMAT(messages.created_at, '%M %d, %Y %h:%i %p') AS 'timestamp', CONCAT(users.first_name, ' ', users.last_name, ' ') AS name FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC")
    print friends
    return render_template('wall.html', my_friends=friends)


@app.route('/login', methods=["POST"])
def login():
    email = request.form['email']
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
    query_data = {'email': email}
    user = mysql.query_db(user_query, query_data)
    if len(user) != 0:
        encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
        if user[0]['password'] == encrypted_password:
            session['user'] = {
                'id': user[0]['id'],
                'first': user[0]['first_name'],
                'last': user[0]['last_name']
            }
            return redirect('/wall')
        else:
            # invalid password!
            flash('invalid password or email!')
        # else:
        #     flash('invalid email!')
        #     # invalid email!
        return redirect('/')
# if email is not equal to email and password not equal to password error
    return redirect('/wall')


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')


@app.route('/post', methods=['POST'])
def post():
    message = request.form['message']
    unique_id = request.form['my_id']
    if len(message) < 20:
        flash('Please input at least 20 characters')
    else:
        query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:my_id, :my_messages, now(), now())"

        data = {
            'my_id': unique_id,
            'my_messages': message
        }
        mysql.query_db(query, data)

    return redirect('/wall')


app.run(debug=True)
