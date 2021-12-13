""" Home app URL Configuration"""

from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/', views.wishlist, name='wishlist'),
]
