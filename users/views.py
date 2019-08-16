from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import RegistrationForm, LoginForm

def register(request):
    #check if the user submitted the post
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created!')
            return redirect('login')
        else:
            messages.error(request, 'Your account was NOT created.')        
    #create blank form otherwise
    else:
        form = RegistrationForm()
    context = {'form' : form, 'title': 'Register' }
    return render(request, 'users/register.html', context)
    

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if not user is None:
                dj_login(request, user)
                return redirect('stocks-portfolio')
            else:
                messages.error(request, 'Invalid email/password combination')
        else:
            messages.error(request, 'Unable to login')
    form = LoginForm()
    context = {'title' : 'login', 'form' : form}
    return render(request, 'users/login.html', context)
