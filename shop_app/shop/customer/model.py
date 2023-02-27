from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Customer:
    name: str
    surname: str
    age: int
    money: Decimal
    preferences: list[int]