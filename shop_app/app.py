from .data_loader.customers_loader import get_customers_data
from .data_loader.products_loader import get_products_data
from .shop.orders.model import OrdersManager
from .shop.service import ShopService
from .logger.model import CustomFormatter, MyLogger

from typing import Final

import logging


def main() -> None:
    """LOGGING"""
    logger = MyLogger.get_logger()

    """APP"""
    logger.warning('STARTING APP')
    CUSTOMERS_PATH: Final = 'shop_app/data/customers.txt'
    PRODUCTS_PATH: Final = 'shop_app/data/products.txt'

    customers = get_customers_data(CUSTOMERS_PATH)

    products = get_products_data(PRODUCTS_PATH)

    om = OrdersManager(customers, products)
    logger.info('Successfully created OrdersManager')

    ss = ShopService(om._get_customers_and_products())
    logger.info('Successfully created ShopService')

    logger.debug('The client who bought the most products')
    print(ss.get_customer_who_bought_most_products())
    logger.debug('The client who spent the most money')
    print(ss.get_customer_who_spent_most_money())
    logger.debug('Statistics about products')
    print(ss.get_statistics_about_products())
    logger.debug('The most popular product')
    print(ss.get_most_popular_product())
    logger.debug('The least popular product')
    print(ss.get_least_popular_product())
    logger.debug('Categories by popularity')
    print(ss.get_categories_by_popularity())

    logger.warning('ENDING APP')
