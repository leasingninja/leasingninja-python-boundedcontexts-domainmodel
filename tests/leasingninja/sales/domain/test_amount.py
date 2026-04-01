import unittest

from leasingninja.sales.domain.Amount import Amount


class AmountTest(unittest.TestCase):
    def test_givenTwoEqualAmounts_whenEquals_thenAreEqual(self):
        # given
        amount1: Amount = Amount(100, "EUR")
        amount2: Amount = Amount(100, "EUR")

        # when
        #are_equal: bool = amount1.equals(amount2)
        are_equal: bool = amount1 == amount2

        # then
        #assertThat(areEqual).isTrue();
        self.assertTrue(are_equal)

    def test_givenTwoUnequalAmounts_whenEquals_thenAreNotEqual(self):
        # given
        amount1: Amount = Amount(100, "EUR")
        amount2: Amount = Amount(200, "EUR")

        # when
        are_equal: bool = amount1 == amount2

        # then
        self.assertFalse(are_equal)

    def test_givenTwoAmountsWithUnequalCurrencies_whenEquals_thenAreNotEqual(self):
        # given
        amount1: Amount = Amount(100, "EUR")
        amount2: Amount = Amount(100, "GBP")

        # when
        are_equal: bool = amount1 == amount2

        # then
        # assertThat(areEqual).isTrue();
        self.assertFalse(are_equal)


if __name__ == '__main__':
    unittest.main()
