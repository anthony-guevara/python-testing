import unittest, os
from src.bank_account import BankAccount
from unittest.mock import patch

from src.exceptions import InsuficientFundsError, WithdrawalTimeRestrictionError


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    def tearDown(self):
        if os.path.exists("transaction_log.txt"):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(1500, self.account.get_balance(), "El balance no es 1500.")

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        assert new_balance == 800
    
    def test_withdraw_with_insuficient_funds(self):
        with self.assertRaises(InsuficientFundsError):
            print(self.account.withdraw(4500))


    def test_get_balance(self):
        assert self.account.get_balance() == 1000

    def test_transaction_log(self):
        new_balance = self.account.deposit(500)

    def test_transaction_log(self):
        self.account.deposit(500)
        assert os.path.exists("transaction_log.txt")

    def test_transaction_log_has_correct_number_of_lines(self):
        self.assertEqual(self._count_lines(self.account.log_file), 1)
        self.account.deposit(500)
        self.assertEqual(self._count_lines(self.account.log_file), 2)

    @patch("src.bank_account.datetime.datetime")
    def test_withdrawal_during_bussiness_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)

    @patch("src.bank_account.datetime.datetime")
    def test_withdrawal_outside_bussiness_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 18
        with self.assertRaises(WithdrawalTimeRestrictionError):
            print(self.account.withdraw(100))

    def test_deposit_various_amounts(self):
        test_cases = [
            {"amount": 100, "expected": 1100},
            {"amount": 3000, "expected": 4000},
            {"amount": 4500, "expected": 5500},
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.account =  BankAccount(balance=1000, log_file="transaction.txt")
                new_balance = self.account.deposit(case["amount"])
                self.assertEqual(new_balance, case["expected"])
