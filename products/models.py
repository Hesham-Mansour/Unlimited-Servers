from typing import Tuple
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_("Title :"), max_length=250)
    title_ar = models.CharField(_("Title-ar :"), max_length=250)

    description = models.TextField(
        _("Description :"), max_length=500, null=True)
    description_ar = models.TextField(
        _("Description-ar :"), max_length=500, null=True)

    # image = models.ImageField(_("image :"), upload_to='image')

    price = models.IntegerField(_("Price :"), null=True, blank=True)
    sale_price = models.IntegerField(_("Sale Price :"), null=True, blank=True)
    months = models.IntegerField(_("Months :"))
    not_1 = models.CharField(
        _("Note 1 :"), max_length=150, null=True, blank=True)
    not_2 = models.CharField(
        _("Note 2 :"), max_length=150, null=True, blank=True)
    not_3 = models.CharField(
        _("Note 3 :"), max_length=150, null=True, blank=True)
    not_4 = models.CharField(
        _("Note 4 :"), max_length=150, null=True, blank=True)
    not_5 = models.CharField(
        _("Note 5 :"), max_length=150, null=True, blank=True)

    def __str__(self):
        return self.title
