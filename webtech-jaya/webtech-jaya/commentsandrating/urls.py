from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_comment_rating, name='add_comment'),
    path('restaurant/<int:restaurant_id>/', views.RestaurantComments.as_view(), name='restaurant_comments'),
]