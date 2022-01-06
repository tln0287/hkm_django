from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _

# Create your models here.


# Create your models here.
class VastrabaranaSeva(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    content = HTMLField(default="<p>Add content</p>")
    image = models.ImageField(upload_to='vastrabaranaseva/',null=True)

    class Meta:
        verbose_name_plural = "VastrabaranaSeva"

class PushpalankaraSeva(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    content = HTMLField(default="<p>Add content</p>")
    image = models.ImageField(upload_to='pushpalankaraseva/',null=True)

    class Meta:
        verbose_name_plural = "PushpalankaraSeva"

class AnnadanaSeva(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    content = HTMLField(default="<p>Add content</p>")
    image = models.ImageField(upload_to='annadanaseva/',null=True)

    class Meta:
        verbose_name_plural = "AnnadanaSeva"

class AbhishekaSeva(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    content = HTMLField(default="<p>Add content</p>")
    image = models.ImageField(upload_to='abhishekaseva/',null=True)

    class Meta:
        verbose_name_plural = "AbhishekaSeva"

class NaivedyaSeva(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    content = HTMLField(default="<p>Add content</p>")
    image = models.ImageField(upload_to='naivedyaseva/',null=True)

    class Meta:
        verbose_name_plural = "NaivedyaSeva"