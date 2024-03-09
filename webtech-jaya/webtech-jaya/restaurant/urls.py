from django.urls import path
from . import views

urlpatterns = [
    path('stationcafe/', views.stationcafe_view, name='stationcafe'),
    path('manjilcafe/', views.manjilcafe_view, name='manjilcafe'),
    path('bishalcafe/', views.bishalcafe_view, name='bishalcafe'),
    path('hungerkills/', views.hungerkills_view, name='hungerkills'),
    path('janata/', views.janata_view, name='janata'),
    path('manakamanacafe/', views.manakamanacafe_view, name='manakamanacafe'),
    path('matkacafe/', views.matkacafe_view, name='matkacafe'),
    path('sarita/', views.sarita_view, name='sarita'),
    path('sitoshna/', views.sitoshna_view, name='sitoshna'),
    
    path('', views.home_view, name='home'),
]
