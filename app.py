from flask import Flask, render_template, request
from money import Money
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/money', methods=['post'])
def money():
    money = Money(request.form['amount'])
    return render_template('money.html', money=money)

if __name__ == '__main__':
    app.run()
