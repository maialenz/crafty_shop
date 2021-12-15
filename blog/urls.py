""" Home app URL Configuration"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name='posts'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
]
