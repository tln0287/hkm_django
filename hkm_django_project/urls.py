from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "HKM"
admin.site.site_title = "HKM"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('', include('About.urls')),
    path('', include('SrilaPrabhupada.urls')),
    path('', include('Temple.urls')),
    path('', include('Gallery.urls')),
    path('', include('festivals.urls')),
    path('', include('Seva.urls')),
    path('', include('contact.urls')),
    path('', include('donate.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

