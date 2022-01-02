from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Temples(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    temple_name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Temples"