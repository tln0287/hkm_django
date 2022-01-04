from django.contrib import admin
from .models import Gallery
# Register your models here.


class GalleryProfileAdmin(admin.ModelAdmin):

    list_display = ['admin_photo']
    list_filter = ['name',]
    readonly_fields = ('admin_photo',)
admin.site.register(Gallery,GalleryProfileAdmin)

