import unittest 
from customer import Customer
from drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.cocktail = Drink("Old Fashioned", 15)
        self.customer = Customer("Brandon", 300)

    def test_drink_has_name(self):
        expected = "Old Fashioned"
        actual = self.cocktail.name 
        self.assertEqual(expected, actual)

