# -*- coding: utf-8 -*-

__author__ = 'Sepehr'
from django import template
register = template.Library()

@register.filter
def module(num):
    num = int(num)
    return ((num % 5) + 1)
