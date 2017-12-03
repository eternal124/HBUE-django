from django.contrib import admin

from .models import *

# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacherId', 'teacherName', )


class ClssAdmin(admin.ModelAdmin):
    list_display = ('classId', 'className', )
    search_fields = ('classClass',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('commentDetail', 'commentCommitTime', 'commentIfPass',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('clss', 'courseOnlyId', 'teacher', 'courseLikes',
                    'courseUnlikes', 'courseCommentNum', 'courseCallRate',
                    'coursePassRate', 'courseGetRate', 'courseLastRate',)


admin.site.register(User)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Clss, ClssAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)
