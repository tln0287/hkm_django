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


class DonatedMember(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    seva_name = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=500, blank=True, null=True)
    amount_paid = models.IntegerField(default =0, null=True, blank=True)
    razorpay_id = models.CharField(max_length=500, blank=True, null=True)
    transaction_date = models.DateTimeField(_("Timestamp"), auto_now=True)
    flag = models.IntegerField(default=0, null=True, blank=True)

class Transaction(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    txn_id = models.CharField(max_length=15,null=True, blank=True)
    phone = models.CharField(max_length=15,null=True, blank=True)
    transaction_type = models.CharField(max_length=60,null=True, blank=True)
    paid_amount = models.CharField(max_length=60,null=True, blank=True)
    balance_amount = models.CharField(max_length=60,null=True, blank=True)
    Date = models.DateField(max_length=255, null=True, blank=True)
    Time = models.CharField(max_length=255, null=True, blank=True)