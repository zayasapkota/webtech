from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_comment_rating, name='add_comment'),
    # Add more URL patterns for other views as needed
]
