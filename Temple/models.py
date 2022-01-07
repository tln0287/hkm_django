from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class TempleHistory(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    content = HTMLField()
    image = models.ImageField(upload_to='temple/', null=True)

    class Meta:
        verbose_name_plural = "Temple History"

class Facilities(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    content = HTMLField()
    image = models.ImageField(upload_to='temple/', null=True)

    class Meta:
        verbose_name_plural = "Facilities"

class GuestHouse(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    content = HTMLField()
    image = models.ImageField(upload_to='temple/', null=True)

    class Meta:
        verbose_name_plural = "Guest House"