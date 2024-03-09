from django.urls import path
from restaurant import views

urlpatterns = [
    # Define URL patterns for the restaurant app
    path('get/', views.restaurant_detail)
]
