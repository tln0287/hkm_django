from django.contrib import admin
from .models import SrilaPrabhupada,Category
# Register your models here.

class CategoryProfileAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title',]

admin.site.register(Category,CategoryProfileAdmin)

class SrilaPrabhupadaProfileAdmin(admin.ModelAdmin):
    list_display = ['content']
    list_filter = ['title',]

admin.site.register(SrilaPrabhupada,SrilaPrabhupadaProfileAdmin)