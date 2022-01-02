from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Festivals(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    content = HTMLField(default="<p>Add content</p>")
    timestamp = models.DateTimeField(_("Timestamp"), auto_now=True)
    event_image = models.ImageField(upload_to='events/')

    class Meta:
        verbose_name_plural = "Festivals"