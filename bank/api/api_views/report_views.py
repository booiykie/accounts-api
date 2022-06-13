from django.db.models import Sum
from slick_reporting.views import SlickReportView
from slick_reporting.fields import SlickReportField
from ..models import User, Client, Account, Transaction, Withdraw, Deposit

import gettext

_ = gettext.gettext


class BankReport(SlickReportView):

    report_model = Account
    date_field = 'open_date'
    group_by = 'client'
    columns = ['name',
               SlickReportField.create(Sum, 'balance', name='sum__balance')]

    chart_settings = [{
        'type': 'column',
        'data_source': ['sum__value'],
        'plot_total': False,
        'title_source': 'Bank Accounts Activity',
        'title': _('Detailed Columns'),

    }, ]


class TransactionsReport(SlickReportView):
    report_model = Transaction
    date_field = 'created_at'
    group_by = 'account__name'
    columns = ['account__name', 'action', 'amount', 'created_at']

    # Analogy for time series
    time_series_pattern = 'daily'
    time_series_columns = [SlickReportField.create(Sum, 'amount', name='sum__amount')]

