from django.contrib import admin
from .models import Question, Choice, UserInfo

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(UserInfo)
# Register your models here.
