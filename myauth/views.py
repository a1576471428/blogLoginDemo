from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView

from myauth.forms import RegisterForm
from myauth.models import BlogUser


def login(request):
    return render(request, "hello.html",context={
        'hello':'helloWorld'
    })


def register(request):
    form = RegisterForm(request.POST)
    if request.method == 'GET':
        return render(request, 'register.html', context={
            'form': RegisterForm()})
    else:
        if form.is_valid():
            user = form.save(True)
            url = '/login'
            return HttpResponseRedirect(url)
        else:
            return render(request, 'register.html', context={
                'form': form
            })
