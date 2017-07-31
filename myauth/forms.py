from django import forms
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import widgets


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'] = forms.CharField(label="用户名：",
                                                  widget=widgets.TextInput(
                                                      attrs={'placeholder': "username", "autofocus": True}))
        self.fields['password1'] =forms.CharField(label='密码：', widget=widgets.PasswordInput(
            attrs={'placeholder': "password"}))
        self.fields['password2'] = forms.CharField(label='再次输入密码：', widget= widgets.PasswordInput(
            attrs={'placeholder': "repeat password"}))
        self.fields['email'] = forms.EmailField(label='邮箱：', widget=widgets.EmailInput
        (attrs={'placeholder': "email"}))
        self.fields['phone'] = forms.CharField(label='手机：', widget=widgets.NumberInput(attrs={
            'placeHolder':'your phone'
        }))



    class Meta:
        model = get_user_model()
        fields = ("username",)

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.phone = self.cleaned_data["phone"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(label='用户名',
                                                  widget=widgets.TextInput(attrs={
                                                      'placeholder':'username',
                                                      'autofocus':True
                                                  }))
        self.fields['password'] = forms.CharField(label='密码',
                                                  widget=widgets.PasswordInput(attrs={
                                                      'placeholder':'password',
                                                  }))
