from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Username",
            'autofocus': ''
        }))
    password = forms.CharField(
        label="密码",
        max_length=256,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': "Password"
        }))
    # captcha = CaptchaField(label="验证码", widget=forms.TextInput(attrs={'class':'form-control'}))
    # captcha = CaptchaField(label="验证码")


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    roles = (
        ('genneral_user', "普通用户"),
        ('admin', "管理员"),
    )
    username = forms.CharField(
        label="用户名",
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))
    password1 = forms.CharField(
        label="密码",
        max_length=256,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        }))
    password2 = forms.CharField(
        label="确认密码",
        max_length=256,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        }))
    email = forms.EmailField(
        label="邮箱地址",
        max_length=256,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
        }))

    sex = forms.ChoiceField(
        label="性别",
        choices=gender,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }))
    # role = forms.ChoiceField(label="角色", choices=roles)
    # captcha = CaptchaField(label="验证码")
class addUserForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    roles = (
        ('genneral_user', "普通用户"),
        ('admin', "管理员"),
    )
    username = forms.CharField(
        label="用户名",
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))
    password = forms.CharField(
        label="密码",
        max_length=256,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        }))
    email = forms.EmailField(
        label="邮箱地址",
        max_length=256,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
        }))

    sex = forms.ChoiceField(
        label="性别",
        choices=gender,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }))
    role = forms.ChoiceField(
        label="注册身份",
        choices=roles,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }))

class getBookForm(forms.Form):
    author = forms.CharField(
        label="作者",
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "作者",
            'autofocus': ''
        }))

    book_name = forms.CharField(
        label="书名",
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "书名",
        }))

    isbn = forms.CharField(
        label="ISBN号",
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "ISBN号",
        }))

    publisher = forms.CharField(
        label="出版社",
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "出版社",
        }))


class addBookForm(forms.Form):
    author = forms.CharField(
        label="作者",
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "作者",
            'autofocus': ''
        }))

    book_name = forms.CharField(
        label="书名",
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "书名",
        }))

    isbn = forms.IntegerField(
        label="ISBN号",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "ISBN号",
        }))

    publisher = forms.CharField(
        label="出版社",
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "出版社",
        }))

    book_count = forms.IntegerField(
        label="馆藏数量",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "馆藏数量",
        }))

    book_remark = forms.CharField(
        label="书籍简介",
        max_length=1024,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "书籍简介",
        }))


class deleteBookForm(forms.Form):
    pass


class getBorrowRecordForm(forms.Form):
    pass


class addBorrowRecordForm(forms.Form):
    
    limit_time = forms.IntegerField(
        label="借书截止时间",
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': "借书截止时间",
        }))

    book_name = forms.CharField(
        label="书名",
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "书名",
        }))

    isbn = forms.IntegerField(
        label="ISBN号",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "ISBN号",
        }))
    pass
    



class deleteBorrowRecordForm(forms.Form):
    pass
