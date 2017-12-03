from django.shortcuts import render
from django.http import Http404
import string

from hbue.models import *



def teachCourse(request, courseId):
    teacherCourses = Course.objects.filter(courseOnlyId=courseId)
    teacher = Teacher.objects.get(teacherId=courseId)

    print(teacherCourses)

    return render(request, "teacher.html", {
        'courseNum': len(teacherCourses),
        'teacherCourses': teacherCourses,
        'teacher': teacher,
        'lastRate_list': [0,2,4,6,8,10]
    })