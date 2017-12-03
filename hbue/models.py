from django.db import models
import django.utils.timezone as timezone

# Create your models here.

# 用户
class User(models.Model):
    course = models.ManyToManyField('Course', through="Comment")#用户和Course表生成的关系表

    userId = models.CharField(max_length=8, primary_key=True, unique=True, null=False)#用户id

    userName = models.CharField(max_length=20)#用户名
    userPassword = models.CharField(max_length=20)#密码
    userEmail = models.CharField(max_length=30)#邮箱
    userPhone = models.CharField(max_length=11)#电话
    userIcon = models.CharField(max_length=20, default='user.png')#用户头像路径，头像文件由用户上传，数据库只存用户头像路径
    userInfo = models.CharField(default="", max_length=300)#用户简介
    userAcademy = models.CharField(max_length=20)#用户所在学院
    userLevel = models.IntegerField(default=1)#用户等级，比如：管理员，常客。。

    def __str__(self):
        return self.userName


# 教师：
class Teacher(models.Model):
    clss = models.ManyToManyField('Clss', through="Course")#教师和Class课程生成的关系表,是确定的课程

    teacherId = models.CharField(max_length=6, primary_key=True, unique=True, null=False)#教师id

    teacherName = models.CharField(max_length=20)#教师名
    teacherIcon = models.CharField(max_length=30)#教师头像路径，同上
    teacherInfo = models.TextField(max_length=300)#教师简介

    def __str__(self):
        return self.teacherName

# 课程（一个课程有多个教师教授，这是课程的大类）
class Clss(models.Model):
    classId = models.CharField(max_length=6, primary_key=True, unique=True, null=False)#课程id

    className = models.CharField(max_length=20)#课程名
    classClass = models.CharField(max_length=20)#课程类型
    classAcademy = models.CharField(max_length=30)#教授学院
    classCredit = models.IntegerField()#学分
    classCapacity = models.IntegerField()#容纳学生数

    def __str__(self):
        return self.className

# 确定课程（由老师和Class确定）
class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.SET)#Teacher的自动生成id是该表的外键
    clss = models.ForeignKey(Clss, on_delete=models.SET)#Class的自动生成id是该表的外键

    courseOnlyId = models.CharField(max_length=12, primary_key=True, unique=True, null=False)#课程唯一id

    courseLikes = models.IntegerField(default=0)#推荐数
    courseUnlikes = models.IntegerField(default=0)#不推荐数
    courseCommentNum = models.IntegerField(default=0)#评论数
    courseCallRate = models.IntegerField(default=0)#点名频率，通过评论计算得出
    coursePassRate = models.IntegerField(default=0)#通过指标
    courseGetRate = models.IntegerField(default=0)#收获指标
    courseLastRate = models.IntegerField(default=5)

    def __str__(self):
        return self.clss.className + '(' + self.teacher.teacherName + ')'


# 用户评价(由User表和Course表确定)
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET) #User自动生成的id是该表的外键，就是，User中的用户被删除了，这条评论也将删除
    course = models.ForeignKey(Course, on_delete=models.SET) #Course自动生成的id是该表的外键，

    commentCallRate = models.IntegerField() #一个用户评价的点名频率，用于计算总评分数
    commentPassRate = models.IntegerField()#同上，通过指标
    commentGetRate = models.IntegerField()#同上，收获指标
    commentDetail = models.TextField(max_length=300)#一个用户的文字评论
    commentCommitTime = models.DateTimeField(default = timezone.now)#评论时间
    commentIfPass = models.BooleanField()#是否通过审核

    def __str__(self):
        return self.user.userName + '(' + self.course.courseOnlyId + ')'

# 推荐
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET)
    course = models.ForeignKey(Course, on_delete=models.SET)

    def __str__(self):
        return 'recommend:' + self.user.userName + ' likes ' + self.course.courseOnlyId




