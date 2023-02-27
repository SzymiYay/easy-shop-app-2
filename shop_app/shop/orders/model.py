from dataclasses import dataclass
from collections import defaultdict

import random


@dataclass
class OrdersManager:
    customers: list[Customer]
    products: list[Product]