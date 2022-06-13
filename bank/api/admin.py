from django.contrib import admin

from .models import User, Client, Account, Transaction, Withdraw, Deposit

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Withdraw)
admin.site.register(Deposit)