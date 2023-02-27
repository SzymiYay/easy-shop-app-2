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