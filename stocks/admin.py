from django.contrib import admin
from stocks.models import Portfolio, Transactions

#registering created models so that they show up on the admin page
admin.site.register(Portfolio)
admin.site.register(Transactions)
