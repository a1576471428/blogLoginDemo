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
    if form.is_valid():
        username = form.cleaned_data['username']
        user = BlogUser.objects.get(username=username)
        if user is not None:
            messages.error(request, '用户已存在')
            return render(request, 'register.html', context={
                'form':form
            })
        else:
            user = form.save(False)
            user.save(True)
            url = reverse('myblog:login')
            return HttpResponseRedirect(url)
    else:
        return render(request, 'register.html', context={
            'form': RegisterForm()
        })
