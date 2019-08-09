from django.urls import path
from stocks import views

urlpatterns = [
    path('', views.home, name='stocks-home'),
    path('portfolio/', views.portfolio, name='stocks-portfolio'),
    path('transactions/', views.transactions, name='stocks-transactions'),
]