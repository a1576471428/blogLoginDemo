from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView
from django.contrib import auth

from myauth.forms import RegisterForm, LoginForm
from myauth.models import BlogUser


def login(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html', context={
            'form':LoginForm
        })
    else:
        form = LoginForm(data=request.POST, request=request) #需要传的参数是data+request， 只传data是不够的!
        if form.is_valid(): #LoginForm继承了AuthenticationForm, 会自动完成认证
            auth.login(request, form.get_user()) #将用户登陆
            redirect_to = request.GET.get('next', '/') #重定向到要访问的地址，没有的话重定向到首页
            return HttpResponseRedirect(redirect_to)
        else: #认证失败
            return render(request, 'auth/login.html', context={
                'form':form
            })


def register(request):
    if request.method == 'GET':
        return render(request, 'auth/register.html', context={
            'form': RegisterForm()})
    else:
        form = RegisterForm(request.POST)
        if form.is_valid(): #RegisterForm继承了UserCreationForm， 会完成用户密码强度检查，用户是否存在的验证
            form.save(True) #认证通过。直接保存到数据库
            url = reverse('myauth:login')
            return HttpResponseRedirect(url)
        else:
            return render(request, 'auth/register.html', context={
                'form': form
            })


def logout(request):
    auth.logout(request)
    redirect_to = '/'
    return HttpResponseRedirect(redirect_to)
