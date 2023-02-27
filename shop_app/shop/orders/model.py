from ..customer.model import Customer
from ..product.model import Product
from ..product.category import Category

from dataclasses import dataclass
from collections import defaultdict

import random


@dataclass
class OrdersManager:
    customers: list[Customer]
    products: list[Product]

    def _get_customers_and_products(self) -> dict[Customer, list[Product]]:
        customers_and_products = {}
        for customer in self.customers:
            customers_and_products[customer] = self._get_products_for_customer(customer)
        return customers_and_products

    def _get_products_for_customer(self, customer: Customer) -> list[Product]:
        customer_preferences = list(map(Category, [int(c) for c in customer.preferences]))
        products_by_category = self._get_products_by_category(self.products)
        products_for_customer = []

        money = customer.money
        for category in customer_preferences:

            product = random.choice(products_by_category[category])
            amount = 0
            while money >= product.price and product.amount > 0:
                money -= product.price
                product.amount -= 1
                amount += 1

            if amount > 0:
                product.amount = amount
                products_for_customer.append(product)

        return products_for_customer

    @staticmethod
    def _get_products_by_category(products: list[Product]) -> dict[Category, list[Product]]:
        products_by_category = defaultdict(list)

        for product in products:
            products_by_category[product.category].append(product)

        return dict(products_by_category)
