from ..product.category import Category
from shop_app.logger.model import MyLogger

import re


def validate_product_data(product_data: list[str]) -> bool:
    errors = {
        'product': product_data[0],
        'name': _validate_product_name(product_data),
        'price': _validate_product_price(product_data),
        'quantity': _validate_product_quantity(product_data),
        'category': _validate_product_category(product_data),
    }

    logger_validator = MyLogger.get_logger()

    if len(errors['name']) != 0 or \
            len(errors['price']) != 0 or \
            len(errors['quantity']) != 0 or \
            len(errors['category']) != 0:
        logger_validator.error(', '.join([f'{k}: {v}' for k, v in errors.items()]))
        return False

    return True


def _validate_product_name(product_data: list[str]) -> list[str]:
    errors = []

    if not re.match(r'^(\w+\s?)+$', product_data[0]):
        errors.append('Must be in format (\w+\s?)+')

    return errors


def _validate_product_price(product_data: list[str]) -> list[str]:
    errors = []

    if not re.match(r'^\d+(\.\d+)?$', product_data[1]) and int(product_data[1]) > 0:
        errors.append('Must be a number and must be positive value')

    return errors


def _validate_product_quantity(product_data: list[str]) -> list[str]:
    errors = []

    if not re.match(r'^\d+$', product_data[2]):
        errors.append('Must be a number')

    return errors


def _validate_product_category(product_data: list[str]) -> list[str]:
    errors = []

    categories = [c.name for c in Category]

    if product_data[3] not in categories:
        errors.append('Must be one of: ' + ', '.join(categories))

    return errors
