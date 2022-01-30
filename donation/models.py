from django.db import models
from io import BytesIO
from django.core.files.storage import default_storage
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from PIL import Image
from tinymce.models import HTMLField

# Create your models here.

class Category(models.Model):
    title = models.CharField(_("Title"), max_length=50)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title

class AddDonation(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_of_donation = models.CharField(max_length=500, blank=True, null=True)
    price = models.IntegerField(default =0, null=True, blank=True)
    image = models.ImageField(upload_to='Donation/', null=True)

    class Meta:
        verbose_name_plural = "Add Donation"

    def __str__(self):
        return self.name_of_donation
