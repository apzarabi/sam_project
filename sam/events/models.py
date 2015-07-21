# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(u"نام دسته", max_length=255, null=False, blank=False)

class Subcategory(models.Model):
    name = models.CharField(u"نام زیردسته", max_length=255, null=False, blank=False)

    category = models.ForeignKey(Category)


class Event(models.Model):
    ACCEPTED = 0
    REJECTED = 1
    PENDING =2
    CONDITION_CHOICES = (
        (ACCEPTED, u"تأیید"),
        (REJECTED, u"رد شده"),
        (PENDING, u"بررسی"),
    )
    name = models.CharField(u"نام رویداد", max_length=255, null=False, blank=False)
    address = models.TextField(u"آدرس", null=False, blank=False)
    description = models.TextField(u"توضیحات", null=False, blank=False)
    condition = models.IntegerField(choices=CONDITION_CHOICES, null=False, blank=False)
    condition_description = models.TextField(u"توضیحات وضعیت", null=False, blank=False)
    verification_file = models.FileField(u"مدرک اعتبار سنجی", null=True, blank=True)

    subcategory = models.ForeignKey(Subcategory)
    # dealer = models.ForeignKey(Dealer)


class EventPicture(models.Model):
    picture = models.ImageField(u"تصویر", upload_to="event_pics", null=False, blank=False)
    event = models.ForeignKey(Event)


class TicketType(models.Model):
    total = models.IntegerField(u"تعداد کل", null=False, blank=False)
    available = models.IntegerField(u"موجود", null=False, blank=False)
    datetime = models.DateTimeField(u"زمان", null=False, blank=False)
    price = models.IntegerField(u"قیمت", null=False, blank=False)

    event = models.ForeignKey(Event)


class Ticket(models.Model):
    column = models.IntegerField(u"ستون", null=True, blank=True)
    row = models.IntegerField(u"ردیف", null=True, blank=True)

    event = models.ForeignKey(Event)
    # order = models.ForeignKey(Order)

class Order(models.Model):
    datetime = models.DateTimeField(u"زمان", null=False, blank=False)

    event = models.ForeignKey(Event)
    # customer = models.ForeignKey(Customer)


class Comment(models.Model):
    text = models.TextField(u"متن", null=False, blank=False)
    datetime = models.DateTimeField(u"زمان", null=False, blank=False)

    event = models.ForeignKey(Event)
    # customer = models.ForeignKey(Customer)


class Rate(models.Model):
    rate_number = models.IntegerField(null=False, blank=False)

    event = models.ForeignKey(Event)
    # customer = models.ForeignKey(Customer)


































