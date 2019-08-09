from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return render
    return HttpResponse('<h1> Home </h1>')

def portfolio(request):
    return HttpResponse('<h1> portfolio </h1>')

def transactions(request):
    return HttpResponse('<h1> transactions </h1>')
