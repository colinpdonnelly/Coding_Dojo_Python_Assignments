from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = 'secret_key'


@app.route('/')
def index():

    if 'number' not in session:
        session['number'] = random.randrange(1, 100)
    if 'text' not in session:
        session['text'] = ''
    # if session.get('number') is None and session.get('text') is None:
        #
        # session['number'] = random.randrange(0, 10)
        # session['text'] = ''
        # print session['number']
        # print session['text']

    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    number = int(request.form['num'])

    if number < session['number']:
        session['text'] = "Your number is too low!"
    elif number > session['number']:
        session['text'] = "Your number is too high!"
    else:
        session['text'] = "Your number is perfect!"

    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session.pop('text')
    session.pop('number')

    return redirect('/')


app.run(debug=True)
