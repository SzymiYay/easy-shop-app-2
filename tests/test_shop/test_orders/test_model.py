from shop_app.shop.orders.model import OrdersManager
from shop_app.shop.customer.model import Customer
from shop_app.shop.product.model import Product
from shop_app.shop.product.category import Category

from decimal import Decimal
import unittest


class TestOrdersManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.customers = [
            Customer(name='Jan', surname='Kowal', age=20, money=Decimal('2000'), preferences='124'),
            Customer(name='Adam', surname='Nowak', age=40, money=Decimal('5000'), preferences='4231')
        ]
        cls.products = [
            Product(name='Phone', amount=3, price=Decimal('2100'), category=Category.ELECTRONICS),
            Product(name='Tomato', amount=200, price=Decimal('5'), category=Category.GROCERIES),
            Product(name='Blender', amount=3, price=Decimal('500'), category=Category.AGD),
            Product(name='Eragon', amount=3, price=Decimal('20'), category=Category.BOOKS),
            Product(name='Oil', amount=10, price=Decimal('20'), category=Category.MOTORIZATION),
            Product(name='Glass', amount=3, price=Decimal('500'), category=Category.MOTORIZATION)
        ]
        cls.om = OrdersManager(cls.customers, cls.products)

    def test_get_products_by_category(self):
        products_by_category = OrdersManager._get_products_by_category(self.products)
        self.assertEqual(6, sum(len(products) for products in products_by_category.values()))
        self.assertEqual(1, len(products_by_category[Category.ELECTRONICS]))
        self.assertEqual(1, len(products_by_category[Category.GROCERIES]))
        self.assertEqual(1, len(products_by_category[Category.AGD]))
        self.assertEqual(1, len(products_by_category[Category.BOOKS]))
        self.assertEqual(2, len(products_by_category[Category.MOTORIZATION]))

    def test_get_products_for_customer(self):
        products_for_customer = self.om._get_products_for_customer(self.customers[0])
        self.assertEqual(2, len(products_for_customer))
        self.assertEqual(200, products_for_customer[0].amount)
        self.assertEqual(3, products_for_customer[1].amount)

        products_for_customer = self.om._get_products_for_customer(self.customers[1])
        self.assertEqual(4, len(products_for_customer))
        self.assertEqual(3, products_for_customer[0].amount)
        self.assertEqual(200, products_for_customer[1].amount)
        self.assertEqual(3, products_for_customer[2].amount)
        self.assertEqual(1, products_for_customer[3].amount)

    def test_get_customers_and_products(self):
        customers_and_products = self.om._get_customers_and_products()
        self.assertEqual(2, len(customers_and_products))
        self.assertEqual(2, len(customers_and_products[self.customers[0]]))
        self.assertEqual(4, len(customers_and_products[self.customers[1]]))


if __name__ == '__main__':
    unittest.main()
