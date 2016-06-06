from decimal import Decimal
from collections import OrderedDict

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
    amount = str(self.amount)
    return amount[:-2] + '.' + amount[-2:]

  def cash(self):
    cash = OrderedDict()
    remaining_total = self.amount
    for key in self.denominations:
      number_required = int(remaining_total/self.denominations[key])
      cash[key] = number_required
      remaining_total -= (self.denominations[key]*number_required)
    return cash