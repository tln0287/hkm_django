from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Category(models.Model):

    title = models.CharField(_("Title"), max_length=50)
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title

class SrilaPrabhupada(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    models.ManyToManyField(
        Category, verbose_name=_("Category"), related_name="post"
    )
    content = HTMLField(default="<p>Add content</p>")
    timestamp = models.DateTimeField(_("Timestamp"), auto_now=True)
    image = models.ImageField(upload_to='events/')
    event_date = models.DateField(null=True,blank=True)

    class Meta:
        verbose_name_plural = "Our Archana"