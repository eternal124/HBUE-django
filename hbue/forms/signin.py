from django import forms
from django.forms import widgets  # 插件

class SignInForm(forms.Form):
    userId = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': u'请输入学号'
        }),
    )

    password = forms.CharField(
        widget=widgets.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': u'请输入密码',
            },
            render_value=True,
        ),
        strip=True,
    )

    remember = forms.BooleanField()