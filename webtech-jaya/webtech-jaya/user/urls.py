from django.urls import path
from . import views
from user.views import SignUpView

urlpatterns = [
    # Other URL patterns for the commentsNrating app
   
    path('', views.index),
    path('login', views.user_login),
    path('signup', views.user_signup),
    path('signup/', SignUpView.as_view(), name='signup'),
    
   
]
