from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "HKM"
admin.site.site_title = "HKM"

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('Home.urls')),
    path('', include('About.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

