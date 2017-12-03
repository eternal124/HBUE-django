from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from hbue.forms import signin, signup
from hbue.models import *

#登录之后跳转页
def index(request):
    username = request.session.get('username','anybody')
    return render('index.html',{
        'username':username
    })


def sin(request):
    if request.method == "POST":
        form = signin.SignInForm(request.POST)
        if form.is_valid():
            userid = form.cleaned_data['userId']
            # 把获取表单的用户名传递给session对象
            request.session['userId'] = userid
            return HttpResponseRedirect(request.URL)
    else:
        form = signin.SignInForm()
    return render('signin.html', {
        'form':form
    })


def sup(request):
    if request.method == 'POST':
        form = signup.SignUpForm(request.POST)

        try:
            if form.is_valid():  # 表单有效
                user = User()
                user.userId = form.cleaned_data['userId']
                user.userName = form.cleaned_data['userName']
                user.password = form.cleaned_data['password']
                user.userAcademy = form.cleaned_data['academy']
                print(user)
                user.save()
                return HttpResponseRedirect('/user/' + user.userId)
            else:  # 表单数据无效
                err_msg = form.errors
                form.password = ""
                form.repassword = ""
                return render(request, "signup.html", {
                    'form': form,
                    'err': err_msg
                })
        except Exception as e:
            # print(e)
            # 跳转到错误页面
            return render(request, "signup.html", {
                'form': form,
            })
    else:
        form = signup.SignUpForm()

    return render(request, "signup.html", {
        'form': form,
    })


def sout(request):
    del request.session['username']  #删除session
    return HttpResponseRedirect(request.URL)


def reset(request):
    return HttpResponse("Reset Password")
