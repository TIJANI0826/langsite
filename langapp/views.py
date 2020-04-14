from django.shortcuts import render, redirect


# Create your views here.
from django.contrib import messages
from .forms import UserRegisterForm
from django_registration.forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('langapp:django_registration_complete')
    else:
        form = RegistrationForm()
    return render(request, 'langapp/accounts/register', {'form': form})


def django_registration_complete(request):
    return render(request, 'django_registration/registration_complete.html')


def login_page(request):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('langapp:django_registration_complete')
    else:
        form = RegistrationForm()
    return render(request, 'langapp/accounts/register', {'form': form})

@login_required(login_url='/langapp/')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/langapp/')
def courses(request):
    return render(request, 'courses.html')

@login_required(login_url='/langap/')
def course(request):
    return render(request, 'course.html')

@login_required(login_url='/langapp/')
def blog(request):
    return render(request, 'blog.html')

@login_required(login_url='/langapp/')
def blog_single(request):
    return render(request, 'blog_single.html')

@login_required(login_url='/langapp/')
def instructors(request):
    return render(request, 'instructors.html')

@login_required(login_url='/langapp/')
def regular(request):
    return render(request, 'regular.html')

@login_required(login_url='/langapp/')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('langapp:home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
