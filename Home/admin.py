from django.contrib import admin
from .models import Slides,Site_Stats
# Register your models here.


admin.site.register(Site_Stats)


class DemoProfileAdmin(admin.ModelAdmin):
    fields = ('name', 'slide_image')
    list_display = ['admin_photo']
    list_filter = ['name',]
    readonly_fields = ('admin_photo',)
admin.site.register(Slides,DemoProfileAdmin)