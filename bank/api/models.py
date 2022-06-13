from django.db import models
import gettext

_ = gettext.gettext


class User(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class Client(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def json_object(self):
        return {
            "name": self.name,
            "address": self.address
        }

    def __str__(self):
        return f"{self.name} - {self.user.name}"


class Account(models.Model):
    SAVINGS = 0
    CREDIT = 1
    # allow account types translation.
    ACCOUNT_TYPES = (
       (SAVINGS, _('SAVINGS')),
       (CREDIT, _('CREDIT')),
    )
    name = models.CharField(max_length=250)
    open_date = models.DateTimeField(auto_now_add=True)
    account_type = models.PositiveSmallIntegerField(choices=ACCOUNT_TYPES, default=SAVINGS)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)

    def json_object(self):
        return {
            "open_date": self.open_date,
            "account_type": self.account_type
        }

    def __str__(self):
        return f"Account: {self.ACCOUNT_TYPES[self.account_type][1]} for {self.client} "


class Transaction(models.Model):
    DEPOSIT = 0
    WITHDRAWAL = 1
    # allow account types translation.
    ACTIONS = (
        (DEPOSIT, _('DEPOSIT')),
        (WITHDRAWAL, _('WITHDRAWAL')),
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    action = models.PositiveSmallIntegerField(choices=ACTIONS, default=DEPOSIT)
    amount = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account} - {self.ACTIONS[self.action][1]} : {self.amount}"


class Withdraw(models.Model):
    amount = models.FloatField()
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return f"Withdrawal: {self.amount} - {self.transaction.id}"


class Deposit(models.Model):
    amount = models.FloatField()
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return f"Deposit: {self.amount} - {self.transaction.id}"
