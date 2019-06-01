from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('Hello World!')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
    return render(request,'index.html')