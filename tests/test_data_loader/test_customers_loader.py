from shop_app.data_loader.customers_loader import get_customers_data
from shop_app.shop.customer.model import Customer

from decimal import Decimal
import unittest


class TestCustomersLoader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('tests/data/customers.txt', 'w') as f:
            f.write('Jan;Kowal;20;2000;124\n')
            f.write('Adam;Nowak;40;5000;4253\n')
            f.write('Joanna;Drwal;23;1500;21\n')

        with open('tests/data/empty.txt', 'w') as f:
            f.write('')

    def test_get_customers_data(self):
        expected_result = [Customer(name='Jan', surname='Kowal', age=20, money=Decimal('2000'), preferences='124'),
                           Customer(name='Adam', surname='Nowak', age=40, money=Decimal('5000'), preferences='4253'),
                           Customer(name='Joanna', surname='Drwal', age=23, money=Decimal('1500'), preferences='21')]
        self.assertEqual(expected_result, get_customers_data('tests/data/customers.txt')[0])

    def test_get_customers_data_invalid_path(self):
        self.assertRaises(FileNotFoundError, get_customers_data, 'tests/data/invalid_path.txt')

    def test_get_customers_data_empty_file(self):
        self.assertEqual([], get_customers_data('tests/data/empty.txt')[0])

    def test_get_customers_data_invalid_data_index_error(self):
        with open('tests/data/invalid_data.txt', 'w') as f:
            f.write('Jan;Kowal;20;2000;124\n')
            f.write('Adam;Nowak;40;5000;4253\n')
            f.write('Joanna;Drwal;23\n')
        self.assertRaises(IndexError, get_customers_data, 'tests/data/invalid_data.txt')

    # def test_get_customers_data_invalid_data_value_error(self):
    #     with open('invalid_data.txt', 'w') as f:
    #         f.write('Jan;Kowal;20;2000;124\n')
    #         f.write('Adam;Nowak;40;5000;4253\n')
    #         f.write(';Drwal;23;2300;123\n')
    #     self.assertRaises(ValueError, get_customers_data, 'invalid_data.txt')


if __name__ == '__main__':
    unittest.main()
