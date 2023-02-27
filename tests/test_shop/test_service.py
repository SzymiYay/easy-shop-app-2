from shop_app.shop.service import ShopService
from shop_app.shop.product.model import Product
from shop_app.shop.product.category import Category
from shop_app.shop.customer.model import Customer

from decimal import Decimal
import unittest


class TestShopService(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.customers_and_products = {
            Customer(name='Jan', surname='Kowal', age=20, money=Decimal('2000'), preferences='124'): [
                Product(name='Earphones', amount=3, price=Decimal('140'), category=Category.ELECTRONICS),
                Product(name='Potato', amount=526, price=Decimal('3'), category=Category.GROCERIES)
            ],
            Customer(name='Adam', surname='Nowak', age=40, money=Decimal('5000'), preferences='4253'): [
                Product(name='Harry Potter', amount=3, price=Decimal('50'), category=Category.BOOKS),
                Product(name='Tomato', amount=200, price=Decimal('5'), category=Category.GROCERIES),
                Product(name='Vacuum', amount=5, price=Decimal('250'), category=Category.AGD)
            ]
        }
        cls.service = ShopService(cls.customers_and_products)

    def test_get_customer_who_bought_most_products(self):
        customer = self.service.get_customer_who_bought_most_products()
        self.assertEqual('Jan', customer.name)
        self.assertEqual('Kowal', customer.surname)
        self.assertEqual(20, customer.age)
        self.assertEqual(Decimal('2000'), customer.money)
        self.assertEqual('124', customer.preferences)

    def test_get_customer_who_spent_most_money(self):
        customer = self.service.get_customer_who_spent_most_money()
        self.assertEqual('Adam', customer.name)
        self.assertEqual('Nowak', customer.surname)
        self.assertEqual(40, customer.age)
        self.assertEqual(Decimal('5000'), customer.money)
        self.assertEqual('4253', customer.preferences)

    def test_get_statistics_about_products(self):
        statistics = self.service.get_statistics_about_products()
        self.assertEqual(3, statistics['Earphones'])
        self.assertEqual(526, statistics['Potato'])
        self.assertEqual(3, statistics['Harry Potter'])
        self.assertEqual(200, statistics['Tomato'])
        self.assertEqual(5, statistics['Vacuum'])

    def test_get_most_popular_product(self):
        product = self.service.get_most_popular_product()
        self.assertEqual('Potato', product)

    def test_get_least_popular_product(self):
        product = self.service.get_least_popular_product()
        self.assertEqual('Earphones', product)

    def test_get_categories_by_popularity(self):
        categories = self.service.get_categories_by_popularity()
        self.assertEqual(Category.GROCERIES, categories[0][0])
        self.assertEqual(726, categories[0][1])
        self.assertEqual(Category.AGD, categories[1][0])
        self.assertEqual(5, categories[1][1])
        self.assertEqual(Category.ELECTRONICS, categories[2][0])
        self.assertEqual(3, categories[2][1])
        self.assertEqual(Category.BOOKS, categories[3][0])
        self.assertEqual(3, categories[3][1])
