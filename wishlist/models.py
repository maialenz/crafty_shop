''' Wishlist app models '''
from django.db import models

from products.models import Product
from profiles.models import UserProfile


class Wishlist(models.Model):
    products = models.ForeignKey(Product, null=False, blank=False,
                                 on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True)

    def __str__(self):
        return self.product.name


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(
        Wishlist, null=False, blank=False, on_delete=models.CASCADE,
        related_name='wishlist_items')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE,
        related_name='wishlist_products')

    def __str__(self):
        return self.product.name
