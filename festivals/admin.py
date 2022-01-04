from django.contrib import admin
from .models import Festivals
# Register your models here.



class FestivalsAdmin(admin.ModelAdmin):

    list_display = ['title','content']
    list_filter = ['title',]

admin.site.register(Festivals,FestivalsAdmin)
