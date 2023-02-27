from .product.model import Product
from .product.category import Category
from .customer.model import Customer
from .orders.model import OrdersManager

from dataclasses import dataclass


@dataclass
class ShopService:
    customers_and_products: dict[Customer, list[Product]]

    def get_customer_who_bought_most_products(self) -> Customer:
        return max(self.customers_and_products.items(),
                   key=lambda pair: sum([product.amount for product in pair[1]])
                   )[0]

    def get_customer_who_spent_most_money(self) -> Customer:
        return max(self.customers_and_products.items(),
                   key=lambda pair: sum([product.price * product.amount for product in pair[1]])
                   )[0]

    def get_statistics_about_products(self) -> dict[Product, int]:
        statistics = {}
        for customer, products in self.customers_and_products.items():
            for product in products:
                if product.name not in statistics.keys():
                    statistics[product.name] = 0
                statistics[product.name] += product.amount
        return statistics

    def get_most_popular_product(self) -> Product:
        return max(self.get_statistics_about_products().items(),
                   key=lambda pair: pair[1])[0]

    def get_least_popular_product(self) -> Product:
        return min(self.get_statistics_about_products().items(),
                   key=lambda pair: pair[1])[0]

    def get_categories_by_popularity(self) -> list[str]:
        categories = {}
        for customer, products in self.customers_and_products.items():
            for product in products:
                if product.category not in categories.keys():
                    categories[product.category] = 0
                categories[product.category] += product.amount
        return sorted(categories.items(), key=lambda pair: pair[1], reverse=True)
