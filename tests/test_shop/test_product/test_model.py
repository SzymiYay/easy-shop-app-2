from shop_app.shop.product.model import Product
from shop_app.shop.product.category import Category

import unittest


class TestCustomer(unittest.TestCase):

    def test_from_list(self):
        product = Product.from_list(['name', '10', '100.00', 'ELECTRONICS'])
        self.assertEqual(product.name, 'name')
        self.assertEqual(product.amount, 10)
        self.assertEqual(product.price, 100.00)
        self.assertEqual(product.category, Category.ELECTRONICS)

    def test_from_list_type_error(self):
        with self.assertRaises(TypeError):
            Product.from_list(['name', '10', '100.00', 'ELECTRONICS', '456'])

    def test_from_list_value_error(self):
        with self.assertRaises(ValueError):
            Product.from_list(['name', 'invalid', '100.00', 'ELECTRONICS'])


if __name__ == '__main__':
    unittest.main()
