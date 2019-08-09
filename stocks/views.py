from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'stocks/home.html')

def portfolio(request):
    return render(request, 'stocks/portfolio.html')

def transactions(request):
    return render(request, 'stocks/transactions.html')
