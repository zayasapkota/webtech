"""
URL configuration for foodfeed project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('restaurants/', include('restaurant.urls')),
    path('comment/', include('commentsandrating.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'), 
    path('login/', auth_views.LoginView.as_view(), name='auth_login'),
    path('', views.index, name='index'),
 
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='auth_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='auth_logout'),
    path('signup/', views.SignUpView.as_view(template_name='login.html'), name='auth_signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    

]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
