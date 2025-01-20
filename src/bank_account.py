import datetime

from src.exceptions import InsuficientFundsError, WithdrawalTimeRestrictionError


class BankAccount:
    def __init__(self, balance=0, log_file=None):
         self.balance = balance
         self.log_file = log_file
         self._log_transaction('Cuenta creada')
    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, 'a') as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposito de {amount}. New Balance: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        now = datetime.datetime.now()
        if amount<0:
            raise ValueError("No puedes retirar una cantidad negativa")
        if now.hour < 8 or now.hour > 17:
            raise WithdrawalTimeRestrictionError("No puedes retirar en este horario")
        if amount > self.balance:
            raise InsuficientFundsError("Saldo insuficiente para hacer el rtiro")
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Retiro de {amount}. New Balance: {self.balance}")
        return self.balance

    def get_balance(self):
        return self.balance
