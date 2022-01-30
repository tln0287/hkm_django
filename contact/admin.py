from django.contrib import admin
from .models import Contact,SocialMedia,ContactQueries



class ContactAdmin(admin.ModelAdmin):

    list_display = ['phone']
    list_filter = ['phone',]

admin.site.register(Contact,ContactAdmin)

class SocialMediaAdmin(admin.ModelAdmin):

    list_display = ['name']
    list_filter = ['name',]

admin.site.register(SocialMedia,SocialMediaAdmin)

class ContactQueriesAdmin(admin.ModelAdmin):

    list_display = ['name','email']
    list_filter = ['name',]

admin.site.register(ContactQueries,ContactQueriesAdmin)
