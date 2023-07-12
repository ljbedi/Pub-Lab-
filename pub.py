from customer import Customer
from drink import Drink 

class Pub: 

        def __init__(self, name, till, drinks): 
                self.name = name 
                self.till = till
                self.drinks = drinks 

        def sell_drink_increase_till(self, drink_to_sell, customer):
                customer.buy_drink(drink_to_sell)
                self.change_till_by_amount(drink_to_sell.price)

