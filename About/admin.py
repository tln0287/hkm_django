from django.contrib import admin
from .models import AboutUs, Team
# Register your models here.


class AboutUsAdmin(admin.ModelAdmin):

    list_display = ['title']
    list_filter = ['title',]

admin.site.register(AboutUs,AboutUsAdmin)


class TeamAdmin(admin.ModelAdmin):

    list_display = ['name']
    list_filter = ['name',]

admin.site.register(Team,TeamAdmin)