from flask import Flask, render_template, request
from decimal import Decimal
from collections import OrderedDict
app = Flask(__name__)

class Money:
  denominations = OrderedDict()
  denominations['50 pound notes'] = 5000
  denominations['20 pound notes'] = 2000
  denominations['10 pound notes'] = 1000
  denominations['5 pound notes'] = 500
  denominations['2 pound coins'] = 200
  denominations['1 pound coins'] = 100
  denominations['50p coins'] = 50
  denominations['20p coins'] = 20
  denominations['10p coins'] = 10
  denominations['5p coins'] = 5
  denominations['2p coins'] = 2
  denominations['1p coins'] = 1

  def __init__(self, amount):
    self.amount=int(Decimal(amount)*100)

  def __repr__(self):
    return str(self.amount/100.00)

  def cash(self):
    cash = []
    remaining_total = self.amount
    for key in self.denominations:
      number_required = int(remaining_total/self.denominations[key])
      cash.append("{denomination}: {number_required}"
                  .format(denomination=key, number_required=number_required))
      remaining_total -= (self.denominations[key]*number_required)
    return cash

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/money', methods=['post'])
def money():
    money = Money(request.form['amount'])
    return render_template('money.html', money=money)

if __name__ == '__main__':
    app.run()
