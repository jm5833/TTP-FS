from django.shortcuts import render, redirect
from django.http import HttpResponse
from stocks.forms import PurchaseForm
from stocks.data_manipulation import *
from django.contrib import messages
from stocks.sdata import is_valid_symbol

def home(request):
    if request.user.is_authenticated:
        return redirect('stocks-portfolio')
    else:
        return redirect('login')

def portfolio(request):
    #redirect user to login if they're not logged in
    if not request.user.is_authenticated:
        messages.warning(request, 'You need to login to view this page')
        return redirect('login')
    #return render(request, 'stocks/home.html')
    #logic if the form was filled out
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            if not is_valid_symbol(form.cleaned_data['stock_ticker']):
                messages.error(request, 'Thats not a valid stock ticker!')
            elif not balance_check(request, form):
                messages.error(request, 'Insufficent balance')
            else:    
                save_transaction(request, form)
                update_portfolio(request, form)
                messages.success(request, 'Stock purchased successfully')
    #display blank form
    current_cash = get_current_cash(request.user.pk)
    form = PurchaseForm()
    user = request.user
    p = get_portfolio(user)
    context = { 'form':form, 
                'title' : 'Portfolio',
                'stocks' : p,
                'portfolio_net' : get_portfolio_net(user),
                'current_cash' : current_cash
              }
    return render(request, 'stocks/portfolio.html', context)

def transactions(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'You need to be logged in to view this page')
        return redirect('login')
    #get a list of the transactions a user has made 
    user_transactions = get_transactions(request.user)
    context = { 'title' : 'Transactions', 'transactions' : user_transactions}
    return render(request, 'stocks/transactions.html', context)
