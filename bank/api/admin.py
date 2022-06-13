import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import User, Client, Account, Transaction, Withdraw, Deposit

admin.site.register(User)
admin.site.register(Client)
# admin.site.register(Account)
# admin.site.register(Transaction)
admin.site.register(Withdraw)
admin.site.register(Deposit)


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("account", "action", "amount", "created_at")
    actions = ["export_as_csv"]
    model = Transaction


@admin.register(Account)
class TransactionAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("name", "open_date", "account_type", "balance", "client")
    actions = ["export_as_csv"]
    model = Account
