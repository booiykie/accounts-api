from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from views import user_views, client_views

urlpatterns = [
    path('users/', user_views.ClientList.as_view()),
    path('users/<int:pk>/', user_views.ClientDetail.as_view()),
    path('clients/', client_views.ClientList.as_view()),
    path('clients/<int:pk>/', client_views.ClientDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
