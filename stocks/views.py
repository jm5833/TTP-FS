from django.shortcuts import render
from django.http import HttpResponse
from stocks.forms import PurchaseForm
from stocks.data_manipulation import save_post

def home(request):
    return render(request, 'stocks/home.html')

def portfolio(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            #create a transaction object
            save_post(request, form)
    else:
        form = PurchaseForm()
    context = {'form':form, 'title' : 'Portfolio'}
    return render(request, 'stocks/portfolio.html', context)
    

def transactions(request):
    return render(request, 'stocks/transactions.html')
