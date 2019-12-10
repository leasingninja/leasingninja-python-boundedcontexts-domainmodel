class Amount:
    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    def amount(self) -> int:
        return self._amount

    def currency(self) -> str:
        return self._currency

    def __eq__(self, other) -> bool:
        return (
            self.__class__ == other.__class__ and
            self._amount == other._amount and
            self._currency == other._currency
        )