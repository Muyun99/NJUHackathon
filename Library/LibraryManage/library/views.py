from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from . import models
from . import forms

# Create your views here.


def index(request):
    if not request.session.get('is_login', None):
        request.session.flush()
        return redirect('/library/login/')
    if (request.method == "GET"):
        book_list = models.Book.objects.all()
        return render(request, 'library/index.html', {'book_list': book_list})
    if (request.method == "POST"):
        return render(request, 'library/index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect('/library/index/')
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
                    return render(request, 'library/login.html', locals())
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/library/index/')
                else:
                    message = "密码不正确"
                    return render(request, 'library/login.html', locals())
    login_form = forms.UserForm()
    return render(request, 'library/login.html', locals())


def register(request):
    if request.session.get('is_login', None):  # 如果登录了就清楚session并跳转
        request.session.flush()
        return redirect('/library/register/')
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
                return render(request, 'library/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = "用户名已存在"
                    return render(request, 'library/register.html', locals())

                same_mail_user = models.User.objects.filter(email=email)
                if same_mail_user:
                    message = "邮箱已存在"
                    return render(request, 'library/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.role = "general_user"
                latest_user = models.User.objects.all()[0]
                new_user.id_number = latest_user.id_number + 1
                new_user.save()
                message = "注册成功！"

                return redirect('/library/login/')
        else:
            return render(request, 'library/register.html', locals())

    register_form = forms.RegisterForm()
    return render(request, 'library/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/library/login/")
    request.session.flush()
    return redirect("/library/login/")


def UserTable(request):
    if (request.method == "GET"):
        user_list = models.User.objects.all()
        getuser_form = forms.getUserForm(request.POST)
        return render(request, 'library/UserTable.html', locals())
    if request.method == "POST":
        getuser_form = forms.getUserForm(request.POST)
        message = "请检查填写的内容！"
        user_list = models.User.objects.all()
        if getuser_form.is_valid():
            id_number = getuser_form.cleaned_data.get('id_number')
            username = getuser_form.cleaned_data.get('username')
            email = getuser_form.cleaned_data.get('email')
            sex = getuser_form.cleaned_data.get('sex')
            role = getuser_form.cleaned_data.get('role')
        if id_number == None:
            id_number=""
        if username == None:
            username=""
        if email == None:
            email=""
        if sex == None:
            sex=""
        if role == None:
            role=""
        if sex == "":
            user_list = models.User.objects.all().filter(
                Q(id_number__contains=id_number),
                Q(name__contains=username),
                Q(email__contains=email),
                Q(sex__contains=sex),
                Q(role__contains=role),
            )
        else:
            user_list = models.User.objects.all().filter(
                Q(id_number__contains=id_number),
                Q(name__contains=username),
                Q(email__contains=email),
                Q(sex=sex),
                Q(role__contains=role),
            )
        if len(user_list) != 0:
            message = "查询成功！"
        else:
            message = "查询失败！请检查您填写的内容"
        # user_list = models.User.objects.all()

        return render(request, 'library/UserTable.html', locals())
        # return render('/library/usertable/', locals())
    getuser_form = forms.getUserForm()
    return render(request, 'library/UserTable.html', locals())


def AddUser(request):
    if (request.method == "GET"):
        user_list = models.User.objects.all()
        adduser_form = forms.addUserForm(request.POST)
        return render(request, 'library/adduser.html', locals())
    if request.method == "POST":
        adduser_form = forms.addUserForm(request.POST)
        message = "请检查填写的内容！"
        user_list = models.User.objects.all()
        if adduser_form.is_valid():
            username = adduser_form.cleaned_data.get('username')
            password = adduser_form.cleaned_data.get('password')
            email = adduser_form.cleaned_data.get('email')
            sex = adduser_form.cleaned_data.get('sex')
            role = adduser_form.cleaned_data.get('role')

            same_name_user = models.User.objects.filter(name=username)
            if same_name_user:
                message = "用户名已存在"
                return render(request, 'library/adduser.html', locals())

            same_mail_user = models.User.objects.filter(email=email)
            if same_mail_user:
                message = "邮箱已存在"
                return render(request, 'library/adduser.html', locals())

            new_user = models.User()
            new_user.name = username
            new_user.password = password
            new_user.email = email
            new_user.sex = sex
            new_user.role = role
            latest_user = models.User.objects.all()[0]
            new_user.id_number = latest_user.id_number + 1
            new_user.save()
            message = "注册成功！"

            return redirect('/library/adduser/', locals())
    adduser_form = forms.addUserForm()
    return render(request, 'library/adduser.html', locals())


def DeleteUser(request):
    if (request.method == "GET"):
        user_list = models.User.objects.all()
        return render(request, 'library/deleteuser.html', locals())


def ChangeUser(request):
    if (request.method == "GET"):
        user_list = models.User.objects.all()
        return render(request, 'library/changeuser.html', locals())


def BookTable(request):
    if (request.method == "GET"):
        book_list = models.Book.objects.all()
        getbook_form = forms.getBookForm(request.POST)
        return render(request, 'library/BookTable.html', locals())
    if request.method == "POST":
        getbook_form = forms.getBookForm(request.POST)
        message = "请检查填写的内容！"
        book_list = models.Book.objects.all()
        if getbook_form.is_valid():
            author = getbook_form.cleaned_data.get('author')
            book_name = getbook_form.cleaned_data.get('book_name')
            isbn = getbook_form.cleaned_data.get('isbn')
            publisher = getbook_form.cleaned_data.get('publisher')
            book_count = getbook_form.cleaned_data.get('book_count')
        if author == None:
            author=""
        if book_name == None:
            book_name=""
        if isbn == None:
            isbn=""
        if publisher == None:
            publisher=""
        if book_count == None:
            book_count=""
        book_list = models.Book.objects.all().filter(
            Q(author__contains=author),
            Q(book_name__contains=book_name),
            Q(isbn__contains=isbn),
            Q(publisher__contains=publisher),
            Q(book_count__contains=book_count), 
        )
        if len(book_list) != 0:
            message = "查询成功！"
        else:
            message = "查询失败！请检查您填写的内容"
        

        return render(request, 'library/BookTable.html', locals())
        # return render('/library/usertable/', locals())
    getbook_form = forms.getBookForm()
    return render(request, 'library/BookTable.html', locals())


def AddBook(request):
    if (request.method == "GET"):
        book_list = models.Book.objects.all()
        addbook_form = forms.addBookForm(request.POST)
        return render(request, 'library/addbook.html', locals())
    # if request.session.get('is_login', None):
    #     return redirect('/library/index/')
    if (request.method == "POST"):
        addbook_form = forms.addBookForm(request.POST)
        if addbook_form.is_valid():
            author = addbook_form.cleaned_data.get('author')
            book_name = addbook_form.cleaned_data.get('book_name')
            isbn = addbook_form.cleaned_data.get('isbn')
            publisher = addbook_form.cleaned_data.get('publisher')
            book_count = addbook_form.cleaned_data.get('book_count')
            book_remark = addbook_form.cleaned_data.get('book_remark')

            new_book = models.Book()
            new_book.author = author
            new_book.book_name = book_name
            new_book.isbn = isbn
            new_book.publisher = publisher
            new_book.book_count = book_count
            new_book.book_remark = book_remark
            new_book.save()

            return redirect('/library/addbook/')

    addbook_form = forms.addBookForm()
    return render(request, 'library/addbook.html', locals())


def DeleteBook(request):
    if (request.method == "GET"):
        book_list = models.Book.objects.all()
        return render(request, 'library/deletebook.html', locals())


def ChangeBook(request):
    if (request.method == "GET"):
        book_list = models.Book.objects.all()
    return render(request, 'library/changebook.html', locals())


def BorrowRecordTable(request):
    if (request.method == "GET"):
        borrowRecord_list = models.BorrowRecord.objects.all()
        return render(request, 'library/BorrowRecordTable.html', locals())


def AddBorrowRecord(request):
    if (request.method == "GET"):
        borrowRecord_list = models.BorrowRecord.objects.all()
        return render(request, 'library/addborrowrecord.html', locals())


def DeleteBorrowRecord(request):
    if (request.method == "GET"):
        borrowRecord_list = models.BorrowRecord.objects.all()
        return render(request, 'library/deleteborrowrecord.html', locals())


def ChangeBorrowRecord(request):
    if (request.method == "GET"):
        borrowRecord_list = models.BorrowRecord.objects.all()
        return render(request, 'library/changeborrowrecord.html', locals())