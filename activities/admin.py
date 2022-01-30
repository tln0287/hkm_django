from django.contrib import admin
from .models import Activities
# Register your models here.



class ActivitiesAdmin(admin.ModelAdmin):

    list_display = ['title',]
    list_filter = ['title',]

admin.site.register(Activities,ActivitiesAdmin)
