from datetime import date
from dataclasses import dataclass

from .Amount import Amount

# ContractNumber = NewType("ContractNumber", str)


@dataclass(frozen=True)
class ContractNumber:
    number: str


@dataclass(frozen=True)
class Customer:
    number: str


@dataclass(frozen=True)
class Car:
    number: str


@dataclass(frozen=True)
class SignDate:
    date: date


class Contract:
    def __init__(self, number: ContractNumber, lessee: Customer, car: Car, price: Amount):
        self._number = number
        self._lessee = lessee
        self._car = car
        self._price: Amount = price
        self._sign_date = None

    def is_signed(self) -> bool:
        return self._sign_date is not None

    def sign(self, date: SignDate) -> None:
        assert not self.is_signed()

        self._sign_date = date

        assert self.is_signed()

    def sign_date(self) -> SignDate:
        assert self.is_signed()
        return self._sign_date
