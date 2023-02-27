from .category import Category

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Product:
    name: str
    amount: int
    price: Decimal
    category: str

    @classmethod
    def from_list(cls, product_data: list[str]) -> 'Product':
        product_data[1] = int(product_data[1])
        product_data[2] = Decimal(product_data[2])

        categories = [c.name for c in Category]

        if product_data[3] not in categories:
            raise ValueError('Category not found')

        product_data[3] = Category[product_data[3]]

        return cls(*product_data)
