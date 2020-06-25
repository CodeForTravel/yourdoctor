from django.contrib import admin

from . import models 

admin.site.register(models.Medicine)
admin.site.register(models.Test)