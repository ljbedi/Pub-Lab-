import unittest 
from customer import Customer
from drink import Drink 

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Liam", 500)
        self.cocktail = Drink("Manhattan", 50)

    def test_buy_a_drink(self):
        self.customer.buy_a_drink(self.cocktail)
        self.assertEqual(450, self.customer.wallet)


