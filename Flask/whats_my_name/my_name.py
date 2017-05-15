from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def hello_world():
    # print 'Hello World'
    # print create_name()
    return render_template('index.html')


@app.route('/process')
def world():
    # print 'Hello World'
    # print create_name()
    return render_template('process.html', in_name=name)


@app.route('/process', methods=['POST'])
def create_name():
    print 'Got Post Info'
    name = request.form['name']
    print request.form['name']
    # return name
    return redirect('/')


app.run(debug='True')
