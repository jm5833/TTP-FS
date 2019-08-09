from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    #check if user has already submitted data to the register form 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #obtain username if the submitted data is valid
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('stocks-home')
    else:
        #use django's builtin signup form
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
