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