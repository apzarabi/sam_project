# -*- coding: utf-8 -*-

__author__ = 'MoTE'
from django import template
register = template.Library()

@register.filter
def farsi_num(eng_int):
    farsi_num = ('۰', '١', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹')
    
    #number = unicode(eng_int).encode('utf-8').strip()
    number = str(eng_int)
    ret = ""
    for digit in number:
        if digit in ('0','1','2','3','4','5','6','7','8','9'):
            ret+=farsi_num[int(digit)]
        else:
            ret+=digit
    return ret