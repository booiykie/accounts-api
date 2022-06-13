from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .api_views.user_views import UserList, UserDetail
from .api_views.client_views import ClientList, ClientDetail
from .api_views.account_views import AccountList, AccountDetail
from .api_views.account_views import TransactionList, TransactionDetail
from .api_views.account_views import WithdrawList, WithdrawDetail
from .api_views.account_views import DepositList, DepositDetail
from .api_views.report_views import BankReport, TransactionsReport

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('clients/', ClientList.as_view()),
    path('clients/<int:pk>/', ClientDetail.as_view()),
    path('account/', AccountList.as_view()),
    path('account/<int:pk>/', AccountDetail.as_view()),
    path('transactions/', TransactionList.as_view()),
    path('transactions/<int:pk>/', TransactionDetail.as_view()),
    path('withdraw/', WithdrawList.as_view()),
    path('withdraw/<int:pk>/', WithdrawDetail.as_view()),
    path('deposit/', DepositList.as_view()),
    path('deposit/<int:pk>/', DepositDetail.as_view()),
    path('accounts_report/', BankReport.as_view()),
    path('transactions_report/', TransactionsReport.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
