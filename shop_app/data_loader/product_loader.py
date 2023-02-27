from ..shop.product.model import Product
from ..shop.validator.product_validator import validate_product_data


def get_products_data(path: str) -> list[Product]:
    with open(path, 'r') as f:
        products_data = [line.strip().split(';') for line in f.readlines()]
        return [Product.from_list(product) for product in products_data if validate_product_data(product)]
