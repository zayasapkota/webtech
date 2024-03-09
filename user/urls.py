from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns for the commentsNrating app
    path('login', views.user_login),
    path('signup', views.user_signup)
]
