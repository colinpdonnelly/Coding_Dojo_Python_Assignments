from flask import Flask, request, redirect, render_template, session, flash
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'secret_key'
mysql = MySQLConnector(app, 'emails')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    email = request.form['email']
    if email == '':
        flash('Email cannot be blank', 'error')
        return redirect('/')
    elif not EMAIL_REGEX.match(email):
        flash('Invalid email address', 'error')
        return redirect('/')
    else:
        query = "INSERT INTO emails(email, created_at, updated_at) VALUES(:email, now(), now())"
        data = {
            'email': email,
            # 'created_at': created_at,
            # 'updated_at': updated_at
        }
        mysql.query_db(query, data)
    return redirect('/success')


@app.route('/success')
def success():
    my_emails = mysql.query_db("SELECT * FROM emails")
    # for my_email in my_emails:

    # print my_emails
    return render_template('success.html', my_emails=my_emails)


# @app.route('/delete', methods=['POST'])
# def delete():
#     id = int(request.form['hidden'])
#     query = "DELETE FROM emails WHERE id = '{}'".format(id)
#     print query
#     mysql.run_mysql_query(query)
#     return redirect('/success')
#

app.run(debug=True)
