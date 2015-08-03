# -*- coding: utf-8 -*-

__author__ = 'MoTE'
from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter
def farsi_num(eng_int):
    print(eng_int)
    farsi_num = ('۰', '١', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹')
    #     farsi_nums = (...)
    number = str(eng_int)
    ret = ""
    for digit in number:
        print(digit)
        if digit in ('0','1','2','3','4','5','6','7','8','9'):
            ret+=farsi_num[int(digit)]
        else:
            ret+=digit
    print(ret)
    return ret