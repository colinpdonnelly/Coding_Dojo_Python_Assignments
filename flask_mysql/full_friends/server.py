from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'full_friend')


@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")

    # for friend in friends:
    #     print friend['name']
    return render_template('index.html', my_friends=friends)


@app.route('/add', methods=['POST'])
def add():
    fullname = request.form['fullname']
    age = request.form['age']
    # since = request.form['created_at']

    query = "INSERT INTO friends (name, age) VALUES (:full_name, :my_age)"

    data = {
        "full_name": fullname,
        "my_age": age,
    }

    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
