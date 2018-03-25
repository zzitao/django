from django.shortcuts import render,redirect
from django.http import HttpResponse
from e_test.models import *

#模板的3层继承
def index(request):
    return render(request,'e_test/index.html')

def base(request):
    return  render(request,'e_test/base.html')

def base_user(request):
    return render(request,'e_test/base_user.html')

def base_goods(request):
    return  render(request,'e_test/base_goods.html')

def user1(request):
    return  render(request,'e_test/user1.html')

def user2(requset):
    return render(requset,'e_test/user2.html')

#CSRF 跨站请求伪造
def crrf1(request):
    return render(request,'e_test/csrf1.html')

def csrf2(request):
    uname = request.POST.get('uname')
    context = {'uname':uname}
    return render(request,'e_test/csrf2.html',context)