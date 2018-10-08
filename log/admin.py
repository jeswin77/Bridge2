# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from log.models import Student,Tutor,Category,StudTutMap
from tutor.models import Subscribers
# Register your models here.

admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(StudTutMap)
admin.site.register(Category)
admin.site.register(Subscribers)
