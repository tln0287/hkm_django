from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Activities(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    content = HTMLField(default="<p>Add content</p>")
    timestamp = models.DateTimeField(_("Timestamp"), auto_now=True)
    active_main_image = models.ImageField(upload_to='Activities/',blank=True, null=True)
    active_image1 = models.ImageField(upload_to='Activities/',blank=True, null=True)
    active_image2 = models.ImageField(upload_to='Activities/',blank=True, null=True)
    active_image3 = models.ImageField(upload_to='Activities/',blank=True, null=True)
    active_image4 = models.ImageField(upload_to='Activities/',blank=True, null=True)
    active_image5 = models.ImageField(upload_to='Activities/',blank=True, null=True)
    active_image6 = models.ImageField(upload_to='Activities/',blank=True, null=True)
    active_image7 = models.ImageField(upload_to='Activities/',blank=True, null=True)
    active_image8 = models.ImageField(upload_to='Activities/',blank=True, null=True)
    active_image9 = models.ImageField(upload_to='Activities/',blank=True, null=True)
    active_image10 = models.ImageField(upload_to='Activities/',blank=True, null=True)
    activity_date = models.DateField(null=True,blank=True)

    class Meta:
        verbose_name_plural = "Add Activity"