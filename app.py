from flask import Flask, render_template, request
from decimal import Decimal
app = Flask(__name__)

class Money:
  def __init__(self, amount):
    self.amount=int(Decimal(amount)*100)

  def __repr__(self):
    return str(self.amount/100.00)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/money', methods=['post'])
def money():
    money = Money(request.form['amount'])
    return render_template('money.html', money=money)

if __name__ == '__main__':
    app.run()
