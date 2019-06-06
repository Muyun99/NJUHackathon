from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms

# Create your views here.


def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/login')
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect('/login/index')
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"

        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            if username.strip() and password:
                # 确保用户名和密码都不为空
                try:
                    user = models.User.objects.get(name=username)
                except:
                    message = "用户不存在"
                    return render(request, 'login/login.html', locals())
                if user.password == password:
                    return redirect('/login/index/')
                else:
                    message = "密码不正确"
                    return render(request, 'login/login.html', locals())
    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/login/index/')
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"

        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')
            if password1 != password2:
                message = "两次输入的密码不相同"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = "用户名已存在"
                    return render(request, 'login/register.html', locals())

                same_mail_user = models.User.objects.filter(email=email)
                if same_mail_user:
                    message = "邮箱已存在"
                    return render(request, 'login/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                message = "注册成功！"

                return redirect('/login/login/')
        else:
            return render(request, 'login/register.html', locals())

    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    pass
    return redirect("/login/index")  # 重定向?
