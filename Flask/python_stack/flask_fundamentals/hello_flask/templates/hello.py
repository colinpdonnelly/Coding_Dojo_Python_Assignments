from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/some_route')
def some_function_name():
    return 'i love jesus'


app.run(debug=True)
