from django.shortcuts import render
from django.http import Http404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import *

def main(request, current_page="1"):
    try:
        current_page = int(current_page)
    except TypeError:
        raise Http404('current_page 失败')

    comments = Comment.objects.filter(commentIfPass=True).order_by('-commentCommitTime')

    paginator = Paginator(comments, 12)
    try:
        data = paginator.page(current_page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    return render(request, "main.html", {
        'comments': data,
        'page_list': paginator.page_range,
        'current_page': current_page,
        'last_page': paginator.num_pages,
    })


