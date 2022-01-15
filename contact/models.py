from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    address = HTMLField()
    email = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Contact Us"
