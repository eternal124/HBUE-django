from django.shortcuts import render
from django.http import Http404, HttpResponse


from ..models import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def All(request, current_page="1", cOrt=""):
    try:
        current_page = int(current_page)
    except TypeError:
        raise Http404('current_page 失败')

    if cOrt != "":
        course_teacher = Course.objects.filter(teacher__teacherName__icontains=cOrt)
        course_class = Course.objects.filter(clss__className__icontains=cOrt)
        courses = course_class | course_teacher
    else :
        courses = Course.objects.all().order_by("-commentNum")

    # 分页 每页显示12条数据
    paginator = Paginator(courses, 12)

    try:
        data = paginator.page(current_page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    # 页面渲染
    return render(request, 'courses.html',{
        'isSearch': False,
        'courses': data,
        'courseNum': len(courses),
        'page_list': paginator.page_range,
        'current_page': current_page,
        'last_page': paginator.num_pages,
        'lastRate_list': [0,2,4,6,8,10],
        'isLogin': request.session['userId'] != ''
    })


def One(request, current_id):
    course = Course.objects.get(courseOnlyId=current_id) # 当前老师的当前课程
    otherCourses = Course.objects.filter(teacher__teacherId=course.teacher.teacherId)
    otherTeachers = Course.objects.filter(clss__classId=course.clss.classId)
    comments = Comment.objects.filter(course__courseOnlyId=course.courseOnlyId)

    # print("搜到的课：", course)
    # print([x for x in range(course.lastRate/2) ])
    print(comments)
    return render(request,"course.html",{
        'course': course,
        'otherCourses': otherCourses,
        'otherTeachers': otherTeachers,
        'lastRate_list': [0, 2, 4, 6, 8, 10],
        'comments': comments

    })

def One(request, id):
    return HttpResponse("Course " + id)

