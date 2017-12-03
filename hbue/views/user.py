from django.shortcuts import render
from django.http import Http404, HttpResponse
import string

from hbue.models import *

# 个人页面
def user_x(request, user_id):
    comments = Comment.objects.filter(user__userId=user_id)
    user = User.objects.get(userId=user_id)

    # like 有问题
    return render(request, "user.html",{
        'commentNum': len(comments),
        'user': user,
        'likeNum': 0,
        'comments': comments,
        'isLogin': 1,
    })

def user_inner(request):
    return HttpResponse("User_Inner")