from django import forms
from django.forms import widgets  # 插件
from django.core.exceptions import ValidationError

import re

from hbue.models import *

class SignUpForm(forms.Form):
    # 初始化下拉列表
    initialSelect = (
        ('经济与环境资源学院', '经济与环境资源学院'),
        ('金融学院', '金融学院'),
        ('财政与公共管理学院', '财政与公共管理学院'),
        ('工商管理学院', '工商管理学院'),
        ('会计学院', '会计学院'),
        ('物流与工程管理学院', '物流与工程管理学院'),
        ('旅游与酒店管理学院', '旅游与酒店管理学院'),
        ('信息管理与统计学院', '信息管理与统计学院'),
        ('法学院', '法学院'),
        ('马克思主义学院', '马克思主义学院'),
        ('艺术设计学院', '艺术设计学院'),
        ('新闻与传播学院', '新闻与传播学院'),
        ('外国语学院', '外国语学院'),
        ('信息工程学院', '信息工程学院'),
        ('体育经济与管理学院', '体育经济与管理学院'),
        ('国际教育学院', '国际教育学院'),
    )
    userId = forms.CharField(
        error_messages={'required': u'学号不能为空'},
        max_length=8,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': u'请输入学号'
        }),
    )
    academy = forms.CharField(
        widget=widgets.Select(   # 插件表现形式为下拉框)
            choices=initialSelect,  # 初始化下拉列表
            attrs={
                'class': 'form-control',
                'placeholder': u'请选择学院',
            },
        ),
    )
    userName = forms.CharField(
        widget=forms.TextInput({
            'class': 'form-control',
            'placeholder': u'请输入用户名'
        })
    )
    password = forms.CharField(
        error_messages = {
            'required': u'密码不能为空!',
            'min_length': u'密码最少为8个字符',
            'max_length': u'密码最多不超过为12个字符!',
        },
        min_length=8,
        max_length=12,
        widget=widgets.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': u'请输入密码(8-12位字母、数字、特殊字符组成)',
            },
            render_value=True,
        ),
        strip=True,
    )
    repassword = forms.CharField(
        widget=widgets.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': u'请再次输入密码',
            },
            render_value=True,
        ),
        strip=True,
        error_messages={'required': '请再次输入密码', }
    )

    def clean_userId(self):
        userid = self.cleaned_data.get('userId')
        users = User.objects.filter(userId=userid).count()
        if users:
            raise ValidationError('该用户已注册！')

        if not re.match(r'^1(4|5|6|7)[0-9]{6}$', str(userid)):
            raise ValidationError('非本校学生，请确认学号信息是否正确！')

        return userid

    def clean_userName(self):
        username = self.cleaned_data.get('userName')
        if username.length == 0:
            raise ValidationError('用户名不可为空')
        return username

    def clean_password(self):
        passwd = self.cleaned_data.get('password')
        passwd_re = re.compile(r'^(?=.{8,12})(((?=.*[A-Z])(?=.*[a-z]))|((?=.*[A-Z])(?=.*[0-9]))|((?=.*[a-z])(?=.*[0-9]))).*$')
        if not passwd_re.match(str(passwd)):
            print(passwd)
            raise ValidationError('密码格式错误')

        return passwd

    def clean_repassword(self):  # 查看两次密码是否一致
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('repassword')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError('两次密码不匹配！')
        return password1

    def clean(self):
        return self.cleaned_data