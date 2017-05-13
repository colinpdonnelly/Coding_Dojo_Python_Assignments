

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    # print username
    print id
    # return username
    return render_template('users.html', username=username)


@app.route('/route/with/<vararg>')
def handler_function(vararg):
    vararg = 'Noel is awesome yeees'
    print vararg
    return vararg


app.run(debug=True)
