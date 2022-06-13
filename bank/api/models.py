from django.db import models
import gettext

_ = gettext.gettext


class User(models.Model):

    def __str__(self):
        return self.name

    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class Client(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def json_object(self):
        return {
            "name": self.name,
            "address": self.address
        }

    def __str_(self):
        return self.name


class Account(models.Model):
    SAVINGS = 1
    CREDIT = 2
    # allow account types translation.
    ACCOUNT_TYPES = (
       (SAVINGS, _('SAVINGS')),
       (CREDIT, _('')),
    )
    name = models.CharField(max_length=250)
    open_date = models.CharField(max_length=250)
    account_type = models.PositiveSmallIntegerField(choices=ACCOUNT_TYPES, default=SAVINGS)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def json_object(self):
        return {
            "open_date": self.open_date,
            "account_type": self.account_type
        }

    def __str__(self):
        return self.account_type


class Transaction(models.Model):

    def __str__(self):
        return str(self.id)

    id = models.IntegerField(primary_key=True, unique=True)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, default=None, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True)
    action = models.CharField(max_length=200)
    amount = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class Withdraw(models.Model):
    amount = models.FloatField()
    transaction = models.ForeignKey(Transaction)


class Deposit(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Account)
    transaction = models.ForeignKey(Transaction)
