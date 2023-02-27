from ..shop.customer.model import Customer
from ..shop.validator.customer_validator import validate_customer_data


def get_customers_data(path: str) -> list[Customer]:
    with open(path, 'r') as f:
        customers_data = [line.strip().split(';') for line in f.readlines()]
        return [Customer.from_list(customer) for customer in customers_data if validate_customer_data(customer)]
