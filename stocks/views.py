from django.shortcuts import render
from django.http import HttpResponse
from stocks.forms import PurchaseForm
from stocks.stock_data import get_stock_data

def home(request):
    return render(request, 'stocks/home.html')

def portfolio(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            s_ticker = form.cleaned_data['stock_ticker']
            post = form.save(commit=False)
            post.user = request.user
            post.price = get_stock_data(s_ticker).get('price')
            post.bought = True
            post.save()
    else:
        form = PurchaseForm()
    context = {'form':form, 'title' : 'Portfolio'}
    return render(request, 'stocks/portfolio.html', context)
    

def transactions(request):
    return render(request, 'stocks/transactions.html')
