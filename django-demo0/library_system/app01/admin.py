from django.contrib import admin
from .models import Question, Choice, UserInfo


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question', {
            'fields': ['question_text']
        }),
        ('Date information', {
            'fields': ['pub_date']
        }),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(UserInfo)
# Register your models here.
