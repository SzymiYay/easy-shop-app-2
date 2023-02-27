from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Product:
    name: str
    amount: int
    price: Decimal
    category: str
