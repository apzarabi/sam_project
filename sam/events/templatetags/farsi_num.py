__author__ = 'MoTE'
from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter
@stringfilter
def farsi_num(eng_int):
    #devanagari_nums = ('०','१','२','३','४','५','६','७','८','९')
    farsi_num = ('۰', '١', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹')
    #     farsi_nums = (...)
    number = str(eng_int)
    return ''.join(farsi_num[int(digit)] for digit in number)