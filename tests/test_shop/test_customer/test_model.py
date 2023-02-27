from shop_app.shop.customer.model import Customer

import unittest


class TestCustomer(unittest.TestCase):

    def test_from_list(self):
        customer = Customer.from_list(['Jan', 'Kowalski', '30', '100.00', '123'])
        self.assertEqual(customer.name, 'Jan')
        self.assertEqual(customer.surname, 'Kowalski')
        self.assertEqual(customer.age, 30)
        self.assertEqual(customer.money, 100.00)
        self.assertEqual(customer.preferences, '123')

    def test_from_list_type_error(self):
        with self.assertRaises(TypeError):
            Customer.from_list(['Jan', 'Kowalski', '30', '100.00', '123', '456'])

    def test_from_list_value_error(self):
        with self.assertRaises(ValueError):
            Customer.from_list(['Jan', 'Kowalski', 'invalid', '100.00', '123'])

    def test_from_list_index_error(self):
        with self.assertRaises(IndexError):
            Customer.from_list(['Jan', 'Kowalski', '30'])


if __name__ == '__main__':
    unittest.main()
