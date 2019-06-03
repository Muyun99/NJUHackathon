from django.shortcuts import render
from django.shortcuts import HttpResponse
from app01 import models

# Create your views here.

user_list = []


def index(request):
    # return HttpResponse('Hello World!')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        models.UserInfo.objects.create(user=username, pwd=password)
        # print(username,password)
        # temp = {'user':username,'pwd':password}
        # user_list.append(temp)
    user_list = models.UserInfo.objects.all()

    return render(request, 'index.html', {'data': user_list})


def polls(request):
    return HttpResponse("Hello,world,You`re at the polls index")


def detail(request, question_id):
    return HttpResponse("You`re looking at question %s." % question_id)


def results(request, question_id):
    response = "You`re looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You`re voting on question %s." % question_id)
