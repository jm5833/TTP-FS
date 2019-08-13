from django.shortcuts import render
from django.http import HttpResponse
from stocks.forms import PurchaseForm
from stocks.data_manipulation import *

def home(request):
    return render(request, 'stocks/home.html')

def portfolio(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            #create a transaction object
            if not balance_check(request, form):
                pass #FIX LATER
            save_transaction(request, form)
            update_portfolio(request, form)
    else:
        form = PurchaseForm()
    context = {'form':form, 'title' : 'Portfolio'}
    return render(request, 'stocks/portfolio.html', context)
    

def transactions(request):
    return render(request, 'stocks/transactions.html')
