#!/usr/bin/env python3
import ipdb

class CashRegister:
  def __init__(self, discount=0):
    self.total = 0
    self.items =[]
    self.discount = discount
    self.last_transaction_price = 0 
    self.last_transaction_quantity = 0
   

  def add_item(self, title, price, quantity=1):
    if quantity > 1:
      for _ in range(quantity):
        self.total += price
        self.items.append(title)
        self.last_transaction_price = price 
        self.last_transaction_quantity = quantity
    else:
      self.total += price
      self.items.append(title)
      self.last_transaction_price = price
      self.last_transaction_quantity = quantity
  pass



  def apply_discount(self):
    if self.discount:
      discount_amount = (self.discount / 100) * self.total
      self.total -= discount_amount
      self.total = round(self.total)
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")


  def void_last_transaction(self):
    for _ in range(self.last_transaction_quantity):
      self.total -= self.last_transaction_price
      self.items.pop()

 

    
