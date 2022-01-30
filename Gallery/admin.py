from django.contrib import admin
from .models import Gallery, WeeklyDarshan,FestivalDarshan,Media,Videos
# Register your models here.


class GalleryProfileAdmin(admin.ModelAdmin):

    list_display = ['admin_photo']
    list_filter = ['name',]
    readonly_fields = ('admin_photo',)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ['youtube_links']
    list_filter = ['name',]
admin.site.register(Gallery,GalleryProfileAdmin)
admin.site.register(WeeklyDarshan,GalleryProfileAdmin)
admin.site.register(FestivalDarshan,GalleryProfileAdmin)
admin.site.register(Media,GalleryProfileAdmin)
admin.site.register(Videos,ProfileAdmin)

