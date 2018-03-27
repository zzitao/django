from django.shortcuts import render,redirect
from df_user.models import *
from hashlib import sha1
from django.http import JsonResponse,HttpResponseRedirect

def register(request):
    context = {'title': '注册'}
    return render(request, 'df_user/register.html', context)

def register_handle(request):
    #接收用户数据
    post = request.POST
    name = post.get('user_name')
    pwd = post.get('pwd')
    email = post.get('email')

    #密码加密
    s1 = sha1()
    s1.update(pwd.encode("utf8"))
    s_pwd = s1.hexdigest()

    #创建对象,并储存到数据库
    user = UserInfo()
    user.name = name
    user.pwd = s_pwd
    user.email =email
    user.save()

    #注册成功转到登录页面
    return redirect('/user/login/')

#通过ajax异步的方式，判断注册时用户名是否存在
def register_exist(request):
    name = request.GET.get('name')
    count = UserInfo.objects.filter(name=name).count()
    print(count)
    return JsonResponse({'count':count})

def login(request):
    name = request.COOKIES.get('name', '')
    context = {'title': '用户登录', 'error_info': 0,  'name': name}
    return render(request, 'df_user/login.html', context)

# 登录处理
def login_handle(request):
    #获取数据
    post = request.POST
    name = post.get('name')
    print("name is %s"%name)
    pwd = post.get('pwd')
    print("pwd is %s"%pwd)
    remember = post.get('remember')
     # 密码加密
    s1 = sha1()
    s1.update(pwd.encode("utf8"))
    s_pwd = s1.hexdigest()
    #验证用户名和密码
    count = UserInfo.objects.filter(name=name, pwd=s_pwd).count()
    print(count)
    if count == 0:#登录失败，用户名或密码错误
        context = {'title': '用户登录', 'error_info': 1, 'name': name,'pwd':pwd}
        return render(request,'df_user/login.html',context)
    else:#登录成功
        user = UserInfo.objects.filter(name=name, pwd=s_pwd)
        red = HttpResponseRedirect('/user/user_center_info')
        #记住用户
        if remember!=0:
            red.set_cookie('name',name)
        else:
            red.set_cookie('name','',max_age=-1)
        request.session['user_id'] = user[0].id
        print("user_id is %d"%user[0].id)
        request.session['name'] = name
        print("name is %s"%name)
        return red

def info(request):
    #根据id获取用户邮箱
    id = request.session['user_id']
    user = UserInfo.objects.filter(id=id)
    email = user[0].email
    print(email)
    name = request.session['name']
    context ={'title':'用户中心','email':email,'name':name }
    return render(request,'df_user/user_center_info.html',context)

def order(request):
    name = request.session['name']
    context = {'title': '用户中心','name':name}
    return render(request, 'df_user/user_center_order.html', context)

def site(request):
    id = request.session['user_id']
    name = request.session['name']
    user = UserInfo.objects.get(id=id)
    if request.method == 'POST':#通过检查post请求，修改地址信息
        post = request.POST
        user.address = post.get('address')
        user.receiver = post.get('receiver')
        user.phone = post.get('phone')
        user.save()
    context = {'title': '用户中心','user':user,'name':name}
    return render(request, 'df_user/user_center_site.html', context)





