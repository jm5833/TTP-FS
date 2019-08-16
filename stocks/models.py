from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from users.models import User

#database table to store a users portfolio information
#    user - user the stock belongs to
#    stock_ticker - stock ticker for the stock that the user owns
#    num_of_shares - integer. number of stocks owned
#    price_bound - price per share paid at the time of purchase
#    date_bought - timedate when the stock was purchases
class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_ticker = models.CharField(max_length=20)
    num_of_shares = models.IntegerField()
    price_bought = models.FloatField()
    date_bought = models.DateTimeField(default=timezone.now)

#database table to store a users transaction information
#    user - user the transaction belongs to 
#    stock_ticker = stock that was bought/sold
#    num_of_shares = number of shares that were used in transaction
#    bought = true if stock was bought. false if it was sold
#    price = price stock was bought/sold at 
class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_ticker = models.CharField(max_length=20)
    num_of_shares = models.IntegerField()
    bought = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    
