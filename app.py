from flask import Flask, render_template, request
from decimal import Decimal
app = Flask(__name__)

class Money:
  def __init__(self, amount):
    self.amount=Decimal(amount)

  def __repr__(self):
    return ('%.2f' % self.amount)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/money', methods=['post'])
def money():
    money = Money(request.form['amount'])
    return render_template('money.html', money=money)

if __name__ == '__main__':
    app.run()
