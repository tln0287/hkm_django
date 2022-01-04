from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe

class Slides(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    slide_image = models.ImageField(upload_to='slides/')

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.slide_image.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Slides"




class Site_Stats(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    our_volunteers = models.IntegerField(null=True)
    global_partners = models.IntegerField(null=True)
    help_children = models.IntegerField(null=True)
    medical_support = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = "Site Statistics"