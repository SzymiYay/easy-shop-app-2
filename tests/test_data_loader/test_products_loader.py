from shop_app.data_loader.products_loader import get_products_data
from shop_app.shop.product.model import Product
from shop_app.shop.product.category import Category

from decimal import Decimal
import unittest


class TestProductsLoader(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with open('tests/data/products.txt', 'w') as f:
            f.write('Washing Machine;4;400;ELECTRONICS\n')
            f.write('Potato;1500;3;GROCERIES\n')
            f.write('Harry Potter;3;50;BOOKS\n')

    def test_get_products_data(self):
        expected_result = [
            Product(name='Washing Machine', amount=4, price=Decimal('400'), category=Category.ELECTRONICS),
            Product(name='Potato', amount=1500, price=Decimal('3'), category=Category.GROCERIES),
            Product(name='Harry Potter', amount=3, price=Decimal('50'), category=Category.BOOKS)
        ]
        result = get_products_data('tests/data/products.txt')

        self.assertEqual(expected_result, result)

    def test_get_products_data_invalid_path(self):
        self.assertRaises(FileNotFoundError, get_products_data, 'tests/data/invalid_path.txt')

    def test_get_products_data_empty_file(self):
        self.assertEqual([], get_products_data('tests/data/empty.txt'))

    # def test_get_products_data_invalid_data_index_error(self):
    #     with open('tests/data/invalid_data.txt', 'w') as f:
    #         f.write('Washing Machine;4;400;ELECTRONICS\n')
    #         f.write('Potato;1500;3;GROCERIES\n')
    #         f.write('Harry Potter;3;50\n')
    #     self.assertRaises(IndexError, get_products_data, 'tests/data/invalid_data.txt')

    # def test_get_products_data_invalid_data_value_error(self):
    #     with open('invalid_data.txt', 'w') as f:
    #         f.write('Washing Machine;4;400;ELECTRONICS\n')
    #         f.write('Potato;1500;3;GROCERIES\n')
    #         f.write(';3;50;BOOKS\n')
    #     self.assertRaises(ValueError, get_products_data, 'invalid_data.txt')


if __name__ == '__main__':
    unittest.main()
