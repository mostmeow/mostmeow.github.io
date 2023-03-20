from django.contrib import admin

from .models import *
# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ['quantity','email','image']
    list_filter = []

admin.site.register(BookingModel, BookingAdmin)
