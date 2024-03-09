# user/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),  # URL name changed to 'login'
    path('signup/', views.user_signup, name='signup'),  # URL name changed to 'signup'
]
