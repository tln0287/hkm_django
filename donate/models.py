from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Donations(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    donation_title = models.CharField(max_length=500, blank=True, null=True)
    donation_required_amount = models.IntegerField(null=True)
    donation_raised = models.IntegerField(null=True)
    content = HTMLField(default="<p>Add content</p>")

    class Meta:
        verbose_name_plural = "Donations"