from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _

# Create your models here.


# Create your models here.
class Archana(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    content = HTMLField(default="<p>Add content</p>")
    image = models.ImageField(upload_to='archana/',null=True)

    class Meta:
        verbose_name_plural = "Archana"

class Biography(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    content = HTMLField(default="<p>Add content</p>")
    image = models.ImageField(upload_to='biography/',null=True)

    class Meta:
        verbose_name_plural = "Biography"

class Books(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    content = HTMLField(default="<p>Add content</p>")
    image = models.ImageField(upload_to='books/',null=True)

    class Meta:
        verbose_name_plural = "Books"

class Lectures(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    file = models.FileField(upload_to='musics/')
    image = models.ImageField(upload_to='lectures/',null=True,blank=True)

    class Meta:
        verbose_name_plural = "Lectures"

    def __str__(self):
        return self.title

class Bhajans(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    file = models.FileField(upload_to='musics/')
    image = models.ImageField(upload_to='bhajans/',null=True,blank=True)

    class Meta:
        verbose_name_plural = "Bhajans"


    def __str__(self):
        return self.title
