from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Customer:
    name: str
    surname: str
    age: int
    money: Decimal
    preferences: list[int]

    @classmethod
    def from_list(cls, data: list[str]) -> 'Customer':
        data[2] = int(data[2])
        data[3] = Decimal(data[3])
        return Customer(*data)
