from django.shortcuts import render, redirect
from django.http import HttpResponse
from stocks.forms import PurchaseForm
from stocks.data_manipulation import *
from django.contrib import messages

def home(request):
    return render(request, 'stocks/home.html')

def portfolio(request):
    #return render(request, 'stocks/home.html')
    #logic if the form was filled out
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            if not balance_check(request, form):
                messages.error(request, 'Insufficent balance')
            save_transaction(request, form)
            update_portfolio(request, form)
            messages.success(request, 'Stock purchased successfully')
    #display blank form
    form = PurchaseForm()
    user = request.user
    p = get_portfolio(user)
    context = { 'form':form, 
                'title' : 'Portfolio',
                'stocks' : p,
                'portfolio_net' : get_portfolio_net(user)
              }
    return render(request, 'stocks/portfolio.html', context)

def transactions(request):
    user_transactions = get_transactions(request.user)
    context = { 'title' : 'Transactions', 'transactions' : user_transactions}
    return render(request, 'stocks/transactions.html', context)
