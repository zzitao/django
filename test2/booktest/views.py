from django.shortcuts import render,redirect
from django.http import HttpResponse
from booktest.models import *

# Create your views here.
def index(request):
    #获取heroinfo对象对应的表中，主键为1的数据
    hero_list = HeroInfo.objects.filter(isDelete=False)
    print(type(hero_list))
    context = { 'hero_list':hero_list}
    return render(request,'booktest/index.html',context)

def detail(request,temp):
    return HttpResponse(temp)

#展示链接页面
def getTest1(request):
    return  render(request,'booktest/getTest1.html')

#接收一键一值得情况
def getTest2(request):
    #根据键获取值
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    #构造上下文
    context = {'a':a1,'b':b1,'c':c1}
    return  render(request,'booktest/getTest2.html',context)

#接收一键多值的情况
def getTest3(request):
    #根据键获取值
    a = request.GET.getlist('a')
    #构造上下文
    context = {'a':a}
    #向模板中传递上下文，并进行渲染
    return  render(request,'booktest/getTest3.html',context)

def postTest1(request):
    return render(request,'booktest/postTest1.html')

def postTest2(request):
    #获取post的值，并把它组成context
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':uhobby}
    return render(request,'booktest/postTest2.html',context)

#练习cookie
def cookieTest(request):
    response = HttpResponse()
    cookie = request.COOKIES
    if 't1' in cookie:
        response.write(cookie['t1'])
    #response.set_cookie('t1','qaz')
    return response

#使用session
def sessionTest1(request):
    uname = request.session.get('myname','None')
    context = {'uname':uname}
    return render(request,'booktest/sessionTest1.html',context)

def sessionTest2(request):
    return render(request,'booktest/sessionTest2.html')

def sessionTest2_handle(request):
    uname = request.POST['uname']
    request.session['myname'] = uname
    request.session.set_expiry(0)
    #使用重定向
    return redirect('/booktest/sessionTest1/')

def sessionTest3(request):
    del request.session['myname']
    return  redirect('/booktest/sessionTest1/')

#使用反向解析
def show(request):
    context = {'id':'awm'}
    return render(request,'booktest/show.html',context)

#使用模板继承
def base1(request):
    return render(request,'booktest/base1.html')

def base2(request):
    return render(request,'booktest/base2.html')