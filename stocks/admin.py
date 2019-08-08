from django.contrib import admin
from .models import Profile, Portfolio, Transactions

#registering created models so that they show up on the admin page
admin.site.register(Profile)
admin.site.register(Portfolio)
admin.site.register(Transactions)
