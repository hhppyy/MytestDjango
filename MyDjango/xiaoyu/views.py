from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from xiaoyu.models import PersonInfo
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_auth(request):
    if request.method == "GET":
        return render(request, "register.html")
    if request.method =="POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        mail = request.POST.get("mail", "")
        #注册账号
        try:
            user = User.objects.create_user(username=username,
                                            password=password,
                                            email=mail)
            return render(request,
                          "register.html",
                          {"msg":"注册成功"})
        except:
            print("%s用户已被注册" %username)
            return render(request,
                          "register.html",
                          {"msg": "%s用户已被注册" %username})

def login_auth(request):
    '''登录认证'''
    if request.method == "GET":
        return render(request, "login_auth.html")

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)
        if user:
            #登录成功
            if user.is_active:
                #登录成功后添加sessionid 用于识别用户的登录状态
                login(request, user)#登录
                # request.session["user"] = username
                # request.session.set_expiry(100)#session失效时间设置
                res = HttpResponseRedirect("/person/")
                res.set_cookie("han","aaaaaaaaaa")
                #return HttpResponseRedirect("/person/")#成功后跳转页面（重定向），注意前边有/
                return res
            else:
                return render(request, "login_auth.html", {"msg": "账号被冻结"})
        else:
            #登录失败，在当期页面停留并提示
            # return JsonResponse({"code":1,"msg":"登录失败"},
            #                     json_dumps_params={'ensure_ascii': False})
            return render(request, "login_auth.html", {"msg": "账号或密码不正确"})


def create_info(request):
    if request.method == "GET":
        return render(request, "create_info.html")

    elif request.method == "POST":
        tel = request.POST.get("tel",0)
        name = request.POST.get("name","")
        age = request.POST.get("age",0)
        mail = request.POST.get("mail","")
        info = PersonInfo.objects.filter(tel=int(tel))
        if info:
            return JsonResponse({"code": 111,
                                 "msg": "已存在",
                                 "date": ""},json_dumps_params={'ensure_ascii': False})
        else:
            info = PersonInfo()
            info.name = name
            info.tel = int(tel)
            info.age = int(age)
            info.mail = mail
            info.save()
            return JsonResponse({"code": 00,
                                 "msg": "添加成功",
                                 "date": ""},json_dumps_params={'ensure_ascii': False})




def get_tel(request):
    if request.method == "GET":
        #从页面上获取tel值
        tel_value = request.GET.get("tel", 1)
        if not tel_value: tel_value=0 #如果是空的就换成0int类型
        #filter 查询
        infos = PersonInfo.objects.filter(tel=int(tel_value))
        print(infos)
        if infos:
            return render(request, "gettel.html", {"info": infos[0]})
        else:
            return render(request, "gettel.html",{"info": {}})


        # try:
        #     print("从页面上获取的tel值：%s" %tel_value)
        #     info = PersonInfo.objects.get(tel=int(tel_value))
        #     print("查询到的结果是object对象：%s" %info)
        # except:
        #     info = {
        #         "name": "",
        #         "age": "",
        #         "mail": ""
        #     }
        # return render(request, "gettel.html",{"info": info})




def htmlView(request):
    context = {
        "titel": "页面自己定义名称"
    }
    return render(request, "artical-1.html", context=context)


# def hello(request):
#     return HttpResponse("hello world")


def navlistView(request):
    nav = [
        {
           "type": "科普读物",
            "value": ["宇宙知识", "百科知识", "科学世界", "生物世界"]
        },
        {
            "type": "计算机/网络",
            "value": ["Java", "Python", "c语言"]
        },
        {
            "type": "建筑",
            "value": ["标准/规范", "室内设计", "建筑科学", "建筑文化"]
        }
    ]

    context = {"nav_name":nav}

    return render(request, "navlist.html", context=context)


def hello(request):
    res = {
        "code": 00,
        "msg": "成功success!",
        "datas": [{"user": "hello"}]
    }

    return JsonResponse(res,
                        json_dumps_params={'ensure_ascii': False})


# def login(request):
#     return render(request, "login.html")

def archive(request, year, month):
    res = {
        "code": 00,
        "msg": "成功success!",
        "datas": [
            {"year": year},
            {"month": month}
        ]
    }

    return JsonResponse(res,
                        json_dumps_params={'ensure_ascii': False})


def demo(request):
    return render(request, "demo.html")

@login_required
def personView(request):
    info = {
        "nicheng": "上海-悠悠",
        "name": "悠悠",
        "age": "20",
        "fancy": ["python", "pytest", "django"],
        "blog": {
            "url": "https://www.cnblogs.com/yoyoketang/",
            "img": "https://pic.cnblogs.com/avatar/1070438/20161126151035.png"
        }
    }

    class Myblog():

        def __init__(self):
            self.name = "yoyo"
            self.age = 20

        def guanzhu(self):
            return "100"

        def fensi(self):
            return "1000"

    #实例化
    blog = Myblog()
    info["myblog"] = blog

    return render(request, "personinfo.html", info)










