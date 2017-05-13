from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def greeting():
    return render_template('index.html')


@app.route('/ninjas')
def ninja():
    return render_template('ninjas.html')


@app.route('/dojos')
def dojo():
    return render_template('dojos.html')


@app.route('/dojos/new', methods=['POST'])
def create_user():

    print 'Got Post info'
    name = request.form['name']
    email = request.form['email']
    print request.form
    return redirect('/dojos')


app.run(debug='True')
