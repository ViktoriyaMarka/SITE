from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import *
from .forms import *

# Create your views here.


def error(request):
    form = ErrorForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        name = request.POST['name']
        disciption = request.POST['disciption']

        send_mail(name,disciption,'edx860@gmail.com',['edx860@gmail.com'],
        fail_silently=False)
        return redirect('/')

    form = ErrorForm()
    context = { 'form':form}
    return render(request, 'feedback/error.html', context)

def question(request):
    form = QuestionForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        name = request.POST['name']
        disciption = request.POST['disciption']

        send_mail(name,disciption,'edx860@gmail.com',['edx860@gmail.com'],
        fail_silently=False)
        return redirect('/')

    form = QuestionForm()
    context = { 'form':form}
    return render(request, 'feedback/question.html', context)

def idea(request):
    form = IdeaForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        name = request.POST['name']
        disciption = request.POST['disciption']

        send_mail(name,disciption,'edx860@gmail.com',['edx860@gmail.com'],
        fail_silently=False)
        return redirect('/')

    form = IdeaForm()
    context = { 'form':form}
    return render(request, 'feedback/idea.html', context)