from django.contrib import admin
from .models import Slides,Clients_Feedback,Site_Stats
# Register your models here.
admin.site.register(Slides)

admin.site.register(Clients_Feedback)
admin.site.register(Site_Stats)
