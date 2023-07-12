import unittest 
from customer import Customer
from drink import Drink 
from pub import Pub

class TestPub (unittest.TestCase):

    def setUp(self):
        self.cocktail = Drink("Old Fashioned", 15)
        self.gin = Drink("Edinburgh Gin", 8)
        self.customer = ("Liam", 500)
        self.pub_name = Pub("Hanover Tap", 500, [self.gin, self.cocktail])

    def sell_drink_increase_till(self):
        self.pub_name.sell_drink_increase_till(self.cocktail, self.customer)
        self.assertEqual(515, self.pub_name.till)
        self.assertEqual(485, self.customer.wallet)

    