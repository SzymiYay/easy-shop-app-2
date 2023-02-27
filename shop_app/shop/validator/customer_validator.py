from ...logger import MyLogger

import logging
import re


def validate_customer_data(customer_data: list[str]) -> bool:
    errors = {
        'customer': f'{customer_data[0]} {customer_data[1]}',
        'name': _validate_customer_name(customer_data),
        'surname': _validate_customer_surname(customer_data),
        'age': _validate_customer_age(customer_data),
        'money': _validate_customer_money(customer_data),
        'preferences': _validate_customer_preferences(customer_data),
    }

    logger_validator = MyLogger.get_logger()

    if len(errors['name']) != 0 or \
            len(errors['surname']) != 0 or \
            len(errors['age']) != 0 or \
            len(errors['money']) != 0 or \
            len(errors['preferences']) != 0:
        logger_validator.error(','.join([f'{k}: {v}' for k, v in errors.items() if len(v) != 0]))
        return False

    return True


def _validate_customer_name(customer_data: list[str]) -> list[str]:
    errors = []

    if not re.match(r'^[A-Z][a-z]+$', customer_data[0]):
        errors.append('Must be in format: [A-Z][a-z]+')

    return errors


def _validate_customer_surname(customer_data: list[str]) -> list[str]:
    errors = []

    if not re.match(r'^[A-Z][a-z]+$', customer_data[1]):
        errors.append('Must be in format: [A-Z][a-z]+')

    return errors


def _validate_customer_age(customer_data: list[str]) -> list[str]:
    errors = []

    if not re.match(r'^\d+$', customer_data[2]):
        errors.append('Must be a number')

    return errors


def _validate_customer_money(customer_data: list[str]) -> list[str]:
    errors = []

    if not re.match(r'^\d+(\.\d+)?$', customer_data[3]) and int(customer_data[3]) > 0:
        errors.append('Must be a number and must be positive value')

    return errors


def _validate_customer_preferences(customer_data: list[str]) -> list[str]:
    errors = []

    if not re.match(r'^\d+$', customer_data[4]):
        errors.append('Must be a string of numbers')

    return errors
