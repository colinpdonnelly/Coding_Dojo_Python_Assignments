from flask import Flask, render_template, session, redirect, request, flash
from mysqlconnection import MySQLConnector
import re
import md5
app = Flask(__name__)

app.secret_key = "IsThisEasyMode"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

mysql = MySQLConnector(app, 'my_wall')


@app.route('/')
def loginreg():
    return render_template('index.html')


@app.route('/wall')
def wall():
    return render_template('wall.html')


@app.route('/register', methods=['POST'])
def register():
    print request.form
    has_errors = False
    if len(request.form['first_name']) == 0:
        flash("First name cannot be blank")
        has_errors = True
    if len(request.form['last_name']) == 0:
        flash("Last name cannot be blank")
        has_errors = True
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not in valid format")
        has_errors = True
    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters long")
        has_errors = True
    if request.form['password'] != request.form['password_confirm']:
        flash("Password field must match password confirmation field")
        has_errors = True

    if has_errors:
        return redirect('/')
    else:
        hashed_password = md5.new(request.form['password']).hexdigest()
        print hashed_password
        query_string = "SELECT * FROM users WHERE email = :emale"
        data = {'emale': request.form['email']}
        found_user = mysql.query_db(query_string, data)
        if found_user:
            flash('Email is already inside the database')
            return redirect('/')
        else:

            query_string = "INSERT INTO users (first_name, last_name, email, password) VALUES (:f_name, :l_name, :emale, :pw)"
            data = {
                'f_name': request.form['first_name'],
                'l_name': request.form['last_name'],
                'emale': request.form['email'],
                'pw': hashed_password
            }
            mysql.query_db(query_string, data)
            # insert into users table
            return redirect('/wall')


app.run(debug=True)
