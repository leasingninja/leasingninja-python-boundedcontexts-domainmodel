class Amount:
    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    def amount(self) -> int:
        return self._amount

    def currency(self) -> str:
        return self._currency
