''' Models for products app '''
from django.db import models


class Category(models.Model):
    ''' Models for category instance '''

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    ''' Models for product instances '''
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=256, null=True, blank=True)
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    price = models.DecimalField(max_digits=6,
                                decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1200,
                                null=True,
                                blank=True)
    image = models.ImageField(null=True,
                              blank=True)

    # Offer size on jewellery for users
    has_sizes = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name
