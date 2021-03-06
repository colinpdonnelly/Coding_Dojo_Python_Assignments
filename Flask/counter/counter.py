from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'hello_world'


@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    print 'counter is {}'.format(session['counter'])

    return render_template('index.html')


@app.route('/two')
def plus_two():
    session['counter'] += 1
    # print 'counter is now {}'.format(session['counter'])
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    # print 'counter is now {}'.format(session['counter'])
    return redirect('/')


app.run(debug='True')
