from django.conf.urls import url,include
from django.contrib import admin
from hbue.views import main,courses,other,sign,teacher,user
from djangotest import settings

urlpatterns = [
    url(r'^$', main.main),  # 主页
    url(r'^main/$', main.main),  # 点击点评后的页面
    url(r'^main(?P<pages>[0-9]+)/$', main.main),  # 点击分页后进行跳转之后的结果
    url(r'^search/(?P<cOrt>[\u4e00-\u9fa5]*)/$', courses.All), # 按课程或教师进行查询
    url(r'^search/(?P<cOrt>[\u4e00-\u9fa5]*)&(?P<pages>[0-9]+)/$', courses.All), # 按课程或教师进行查询并翻页
    url(r'^courses/$', courses.All),  # 所有的课程页
    url(r'^courses/(?P<pages>[0-9]+)/$', courses.All),  # 点击分页后进行跳转之后的结果
    url(r'^course/([a-zA-Z]{2}[0-9]{4}[a-zA-Z]{2}[0-9]{4})/$', courses.One), # 单个课程页，即课程详细点评页 点击老师课程名跳转
    url(r'^course/([a-zA-Z]{2}[0-9]{4}[a-zA-Z]{2}[0-9]{4})/#comment-[0-9]{6}/$', courses.One), # 点击评论里的更多 跳转到相应的course下的锚点
    url(r'^signin/$', sign.sin),  # 登录页面
    url(r'^signup/$', sign.sup),  # 注册页面
    url(r'^reset/$', sign.reset), # 密码重置
    url(r'^user/([0-9]{8})/$', user.user_x), # 未登录时别人看到的
    url(r'^user/([0-9]{8})/follow/$', user.user_x),  # 关注的人
    url(r'^user/([0-9]{8})/comments/$', user.user_x),  # 该用户所有的评论
    url(r'^user/inner/([0-9]{8})/$', user.user_inner), # 登录或者注册过后进行跳转 用户id 未明确
    url(r'^teacher/([a-zA-Z]{2}[0-9]{4})/$', teacher.teachCourse), # 点击老师姓名时 跳转 显示该老师所有的课程1
    url(r'^about/$', other.about), # 关于我们
    url(r'^blog/$', other.blog), # 博客
    url(r'^community-rule/$', other.rule),  # 使用规则

    url(r'^admin/', admin.site.urls),
]
