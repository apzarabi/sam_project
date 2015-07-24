# -*- coding: utf-8 -*-
import uuid
from django.db import models

from users.models import Dealer, Customer

def get_picture_path(instance, filename):
    """ this function is derived from a function by amirali moinfar for webcourse spring 2015."""
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'pictures/' + filename


class Category(models.Model):
    name = models.CharField(u"نام دسته", max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = u"دسته"
        verbose_name_plural = u"دسته‌ها"

    def __unicode__(self):
            return u"دسته {}".format(self.name)


class Subcategory(models.Model):
    name = models.CharField(u"نام زیردسته", max_length=255, null=False, blank=False)

    category = models.ForeignKey(Category)

    class Meta:
        verbose_name = u"زیردسته"
        verbose_name_plural = u"زیردسته‌ها"

    def __unicode__(self):
        return u"زیردسته‌ی {} در دسته‌ی {}".format(self.name, self.category.name)


class Event(models.Model):
    ACCEPTED = 0
    REJECTED = 1
    PENDING = 2
    CONDITION_CHOICES = (
        (ACCEPTED, u"تأیید"),
        (REJECTED, u"رد شده"),
        (PENDING, u"بررسی"),
    )
    name = models.CharField(u"نام رویداد", max_length=255, null=False, blank=False)
    address = models.TextField(u"آدرس", null=False, blank=False)
    description = models.TextField(u"توضیحات", null=False, blank=False)
    condition = models.IntegerField(u"وضعیت", choices=CONDITION_CHOICES, default=2, null=False, blank=False)
    condition_description = models.TextField(u"توضیحات وضعیت", null=False, blank=False)
    verification_file = models.FileField(u"مدرک اعتبار سنجی", null=True, blank=True)
    latitude = models.FloatField(u"عرض جغرافیایی", null=False, blank=False)
    longitude = models.FloatField(u"طول جغرافیایی", null=False, blank=False)

    subcategory = models.ForeignKey(Subcategory)
    dealer = models.ForeignKey(Dealer)

    class Meta:
        verbose_name = u"رویداد"
        verbose_name_plural = u"رویدادها"

    def __unicode__(self):
        return u"رویداد {} ".format(self.name)

class EventPicture(models.Model):
    picture = models.ImageField(u"تصویر", upload_to=get_picture_path, null=False, blank=False)
    event = models.ForeignKey(Event)

    class Meta:
        verbose_name = u"تصویر رویداد"
        verbose_name_plural = u"تصاویر رویدادها"

    def __unicode__(self):
        return u"تصویر برای رویداد {}".format(self.event.name)


class TicketType(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    total = models.IntegerField(u"تعداد کل", null=False, blank=False)
    available = models.IntegerField(u"موجود", null=False, blank=False)
    datetime = models.DateTimeField(u"زمان", null=False, blank=False)
    price = models.IntegerField(u"قیمت", null=False, blank=False)

    event = models.ForeignKey(Event)

    class Meta:
        verbose_name = u"نوع‌بلیط"
        verbose_name_plural = u"نوع‌بلیط‌ها"

    def __unicode__(self):
        return u"{}".format(self.name)


class Order(models.Model):
    datetime = models.DateTimeField(u"زمان", null=False, blank=False)

    event = models.ForeignKey(Event)
    customer = models.ForeignKey(Customer)

    class Meta:
        verbose_name = u"سفارش"
        verbose_name_plural = u"سفارش‌ها"


class Ticket(models.Model):
    column = models.IntegerField(u"ستون", null=True, blank=True)
    row = models.IntegerField(u"ردیف", null=True, blank=True)

    event = models.ForeignKey(Event)
    order = models.ForeignKey(Order)

    class Meta:
        verbose_name = u"بلیط"
        verbose_name_plural = u"بلیط‌ها"


class Comment(models.Model):
    text = models.TextField(u"متن", null=False, blank=False)
    datetime = models.DateTimeField(u"زمان", null=False, blank=False)

    event = models.ForeignKey(Event)
    customer = models.ForeignKey(Customer)

    class Meta:
        verbose_name = u"نظر"
        verbose_name_plural = u"نظرها"


class Rate(models.Model):
    rate_number = models.IntegerField(null=False, blank=False)

    event = models.ForeignKey(Event)
    customer = models.ForeignKey(Customer)

    class Meta:
        verbose_name = u"امتیاز"
        verbose_name_plural = u"امتیازها"


































