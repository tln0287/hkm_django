from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class AboutUs(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    content = HTMLField(default="<p>Add content</p>")
    about_image = models.ImageField(upload_to='about/',null=True)

    class Meta:
        verbose_name_plural = "About Us"


class Team(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    designation = models.CharField(max_length=500, blank=True, null=True)
    photo = models.ImageField(upload_to='team/',null=True)
    facebook = models.CharField(max_length=500, blank=True, null=True)
    instagram = models.CharField(max_length=500, blank=True, null=True)
    youtubechannel = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Team"

    def __str__(self):
        return self.name
