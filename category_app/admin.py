from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Locations)
admin.site.register(BusinessServices)