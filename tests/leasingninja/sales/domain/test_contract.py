import unittest
from datetime import date

from leasingninja.sales.domain.Contract import Contract, ContractNumber, Customer, Car, SignDate

from leasingninja.sales.domain.Amount import Amount


class ContractTest(unittest.TestCase):
    def test_givenANewContract_whenSign_thenContractIsSigned(self):
        # given
        contract = Contract(ContractNumber("4711"),
                            Customer("John Buyer"),
                            Car("Volkswagen ID.3"),
                            Amount(20_000, "EUR"))

        # when
        contract.sign(SignDate(date(2018, 12, 24)))

        # then
        self.assertTrue(contract.is_signed())
        self.assertEqual(contract.sign_date(), SignDate(date(2018, 12, 24)))
        # check that event ContractSigned is fired


if __name__ == '__main__':
    unittest.main()
