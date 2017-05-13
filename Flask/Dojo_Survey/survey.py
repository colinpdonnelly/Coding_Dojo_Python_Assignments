from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = 'secret_key'


@app.route('/')
def index():

    if session.get('number') is None and session.get('text') is None:

        session['number'] = random.randrange(0, 101)
        session['text'] = ''

    return render_template('index.html', text=session['text'])


@app.route('/guess', methods=['POST'])
def guess():
    number = int(request.form['number'])

    if number < session['number']:
        session['text'] = "low"
    elif number > session['number']:
        session['text'] = "high"
    else:
        session['text'] = "perfect"

    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session.pop('text')
    session.pop('number')

    return redirect('/')


app.run(debug=True)
