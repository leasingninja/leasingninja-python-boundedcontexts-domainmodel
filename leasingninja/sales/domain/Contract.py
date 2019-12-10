from .Amount import Amount


class Contract:
    def __init__(self, number, lessee, car, price: Amount):
        self._number = number
        self._lessee = lessee
        self._car = car
        self._price: Amount = price
        self._sign_date = None

    def is_signed(self) -> bool:
        return self._sign_date is not None

    def sign(self, date) -> None:
        assert not self.is_signed()

        self._sign_date = date

        assert self.is_signed()

    def sign_date(self):  #-> SignDate:
        assert self.is_signed()
        return self._sign_date
