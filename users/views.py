from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

from django.contrib.auth import authenticate, login


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        #
        ...
    else:
        # Return an 'invalid login' error message.
        ...


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('langapp:home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

