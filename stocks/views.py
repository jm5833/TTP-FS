from django.shortcuts import render, redirect
from django.http import HttpResponse
from stocks.forms import PurchaseForm
from stocks.data_manipulation import *
from django.contrib import messages

def home(request):
    return render(request, 'stocks/home.html')

def portfolio(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            if not balance_check(request, form):
                messages.error(request, 'Insufficent balance')
                return redirect('stocks-portfolio')
            save_transaction(request, form)
            update_portfolio(request, form)
            return redirect('stocks-portfolio')
    else:
        form = PurchaseForm()

    context = {'form':form, 'title' : 'Portfolio'}
    return render(request, 'stocks/portfolio.html', context)
    

def transactions(request):
    return render(request, 'stocks/transactions.html')
