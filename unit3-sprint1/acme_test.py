import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    def test_default_product_price(self):
        """ Testing to see if default price is 10. """
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """ Testing to see if default weight is 20. """
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_flammability(self):
        """ Testing to see if default flammability is 10. """
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_stealability_and_explode(self):
        """ Tests stealability and explode functions """
        prod = Product(name='Test Product', price=100,
                       weight=100, flammability=100)
        self.assertEqual(prod.stealability(), "Very stealable!")
        self.assertEqual(prod.explode(), "...BABOOM!!")


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        """ Testing to see if default generated product is 30. """
        case = generate_products()
        self.assertEqual(len(case), 30)

    def test_legal_names(self):
        """ Testing to see if names are legal. """
        case = generate_products()
        for product in case:
            adjective, noun = product.name.split()
            self.assertIn(adjective, ADJECTIVES)
            self.assertIn(noun, NOUNS)

if __name__ == '__main__':
    unittest.main()