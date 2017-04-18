from django.contrib import admin
from main.models import *
# Register your models here.

admin.site.register(ExceptionMessage)
admin.site.register(Source)
admin.site.register(ExceptionMessageDetail)