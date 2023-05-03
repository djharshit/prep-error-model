"""This is a simple server to deploy the model"""

import random

from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    """ Home page with request method GET and POST
    """
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        sentence = request.form.get('sentence')
        print(sentence)

        if sentence == '':
            return render_template('index.html')

        return redirect('/result')


@app.route('/result')
def result_page():
    """ Result page with result and accuracy
    """
    result = random.choice(['correct', 'incorrect'])
    accuracy = 60 + random.uniform(0.0, 1.0)*10

    return render_template('result.html', result=result, accuracy=accuracy)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6060, debug=True)
