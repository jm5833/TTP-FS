from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import RegisterForm

def register(request):
    #check if user has already submitted data to the register form 
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        #check if submitted data is valid data
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        #use created registration form
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Register'})
