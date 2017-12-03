from django import forms
from django.forms import widgets  # 插件
from django.core.exceptions import ValidationError

import re

from hbue.models import *

class ResetForm(forms.Form):
    password = forms.CharField(
        error_messages={
            'required': u'密码不能为空!',
            'min_length': u'密码最少为8个字符',
            'max_length': u'密码最多不超过为12个字符!',
        },
        min_length=8,
        max_length=12,
        widget=widgets.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': u'请输入密码(8-12位数字,字母或_.组成)',
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