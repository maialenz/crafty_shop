""" Home app URL Configuration"""

from django.urls import path
from . import views

urlpatterns = [
   path('review/<product_id>/', views.add_review,
        name='add_review'),
]
