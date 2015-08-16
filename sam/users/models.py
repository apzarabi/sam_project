# -*- coding: utf-8 -*-

import uuid
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


def get_user_avatar_path(instance, filename):
    """ this function is derived from a function by amirali moinfar for webcourse spring 2015."""
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'avatars/' + filename


class UserInfo(models.Model):
    """ Additional information for normal django user. """
    user = models.OneToOneField(User, null=False, blank=False)
    picture = models.ImageField(u"تصویر", upload_to=get_user_avatar_path, null=False, blank=False)
    datetime = models.DateTimeField(u"تاریخ عضویت", default=timezone.now, null=False, blank=False)

    def get_class(self):
        return "userInfo"

    def __unicode__(self):
        return u"اطلاعت پایه‌ای کاربر {}".format(self.user.username)

class Customer(models.Model):
    """ Additional information for customers for UserInfo. """
    userInfo = models.OneToOneField(UserInfo, null=False, blank=False)
    date = models.DateField(u"تاریخ تولد", default=datetime.date(1990, 1, 1), null=False, blank=False)

    class Meta:
        verbose_name = u"خریدار"
        verbose_name_plural = u"خریداران"

    def get_class(self):
        return "customer"

    def __unicode__(self):
        return u"خریدار {}".format(self.userInfo.user.username)


class Dealer(models.Model):
    """ Additional infromation for dealers for UserInfo. """
    ACCEPTED = 0
    REJECTED = 1
    PENDING = 2
    CONDITION_CHOICES = (
        (ACCEPTED, u"تأیید شده"),
        (REJECTED, u"رد شده"),
        (PENDING, u"بررسی"),
    )
    condition = models.IntegerField(u"وضعیت", choices=CONDITION_CHOICES, default=2, null=False, blank=False)
    condition_description = models.TextField(u"توضیحات وضعیت", null=False, blank=False)
    userInfo = models.OneToOneField(UserInfo, null=False, blank=False)
    registryNumber = models.CharField(u"شماره‌ی ثبت", max_length=10, null=False, blank=False, unique=True)
    certificate = models.FileField(u"مدرک اعتبار سنجی", upload_to='certifications/', null=True, blank=True)

    class Meta:
        verbose_name = u"فروشنده"
        verbose_name_plural = u"فروشندگان"

    def get_class(self):
        return "dealer"

    def __unicode__(self):
        return u"فروشنده {}".format(self.userInfo.user.username)

    def get_status(self):
        return  self.CONDITION_CHOICES[self.condition][1]
    














