from django.urls import path
from . import views

urlpatterns = [
    path('add-comment/', views.add_comment, name='add_comment'),
    path('add-rating/', views.add_rating, name='add_rating'),
    # Add more URL patterns for other views as needed
]
