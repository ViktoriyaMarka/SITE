from django.shortcuts import render, redirect
from .forms import CreateUserFrom
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.

def index(request):
    files = File.objects.latest()
    context = {'files': files}
    return render(request, 'app/index.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserFrom()

        if request.method == 'POST':
            form = CreateUserFrom(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Аккаунт ' +  user + ' успешно зарегистрирован')

                return redirect('login')


        context = {'form': form}
        return render(request, 'app/accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
        
        return render(request, 'app/accounts/login.html')

def logoutPage(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def functions(request):
    elements = Function.objects.all()
    context = {'elements':elements}
    return render(request, 'app/functions.html', context)

@login_required(login_url='login')
def manual(request):
    elements = Manual.objects.all()
    context = {'elements':elements}
    return render(request, 'app/manual.html', context)

@login_required(login_url='login')
def system(request):
    system_app = System_App.objects.all()
    system_prog = System_Prog.objects.all()
    context = {'system_app':system_app,'system_prog':system_prog }
    return render(request, 'app/system.html', context)
