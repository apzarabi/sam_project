# -*- coding: utf-8 -*-

import re

from django import forms
from django.contrib.auth.models import User

from .models import UserInfo, Customer, Dealer

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=80, widget=forms.PasswordInput)
    re_password = forms.CharField(max_length=80, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'type': "email",
                                                     'class': "form-control",
                                                     'id': "password",
                                                     'placeholder': u"رمز عبور",
                                                     })
        self.fields['re_password'].widget.attrs.update({'type': "email",
                                                        'class': "form-control",
                                                        'id': "re_password",
                                                        'placeholder': u"تکرار رمز عبور",
                                                        })
        self.fields['email'].widget.attrs.update({'type': "email",
                                                  'class': "form-control",
                                                  'id': "email",
                                                  'placeholder': u"ایمیل",
                                                  })
        self.fields['username'].widget.attrs.update({'type': "text",
                                                     'class': "form-control",
                                                     'id': "username",
                                                     'placeholder': u"نام کاربری",
                                                     })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError(u"باید آدرس ایمیل خود را وارد کنید.", code='required')
        if not EMAIL_REGEX.match(email):
            raise forms.ValidationError(u"آدرس ایمیل معتبر وارد کنید.")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(u"این آدرس ایمیل قبلا در سامانه ثبت شده است.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password is None or len(password) < 6:
            raise forms.ValidationError(u"رمز عبور باید حداقل ۶ حرف داشته باشد.", code='invalid')
        return password

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError(u"دو رمز یکسان نیستند.", code='invalid')
        return re_password

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['picture']

    def __init__(self, *args, **kwargs):
        super(UserInfoForm, self).__init__(*args, **kwargs)
        self.fields['picture'].widget.attrs.update({'type': "file",
                                                  'id': "picture",
                                                  })

class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = ['registryNumber', 'certificate']

    def __init__(self, *args, **kwargs):
        super(DealerForm, self).__init__(*args, **kwargs)
        self.fields['registryNumber'].widget.attrs.update({'type': "number",
                                                           'class': "form-control",
                                                           'id': "registry_number",
                                                           'placeholder': u"شماره‌ی ثبت",
                                                           })
        self.fields['certificate'].widget.attrs.update({'type': "file",
                                                        'id': "certificate",
                                                        })


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['date']

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'type': "date",
                                                  'class': "form-control",
                                                  'id': "customer_date",
                                                  'placeholder': u"تاریخ",
                                                  })
