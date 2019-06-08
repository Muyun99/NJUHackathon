from django.db import models

# Create your models here.


class User(models.Model):
    gender = (('male', "男"), ('female', "女"))
    roles = (('genneral_user', "普通用户"), ('admin', "管理员"))

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    id_number = models.BigIntegerField(unique=True)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    role = models.CharField(max_length=32, choices=roles, default="普通用户")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class Book(models.Model):
    author = models.CharField(max_length=128)
    book_name = models.CharField(max_length=128)
    isbn = models.BigIntegerField(unique=True)
    publisher = models.CharField(max_length=128)
    book_count = models.IntegerField()
    book_remark = models.CharField(max_length=1024)


class BorrowRecord(models.Model):
    id_number = models.ForeignKey(to='User', to_field='id_number', on_delete=models.CASCADE)
    isbn = models.ForeignKey(to='Book', to_field='isbn', on_delete=models.CASCADE)
    borrow_time = models.DateTimeField(auto_now_add=True)
    limit_time = models.IntegerField()
