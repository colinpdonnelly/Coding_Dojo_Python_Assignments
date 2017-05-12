from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def formula():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def info():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    return render_template('result.html', name=name, location=location, language=language, comment=comment)


@app.route('/clear')
def clear():
    return redirect('/')


app.run(debug='True')
