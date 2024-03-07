from django.urls import path
from restaurant import views

urlpatterns = [
     path('stationcafe/', views.stationcafe_view, name='stationcafe'),
     path('manjilcafe/', views.manjilcafe_view, name='manjilcafe'),
     path('janata/', views.janata_view, name='janata'),
     path('hungerkills/', views.hungerkills_view, name='hungerkills'),
     path('bishalcafe/', views.bishalcafe_view, name='bishalcafe'),
     path('manakamanacafe/', views.manakamanacafe_view, name='manakamanacafe'),
     path('matkacafe/', views.matkacafe_view, name='matkacafe'),
     path('sarita/', views.sarita_view, name='sarita'),
     path('sitoshna/', views.sitoshna_view, name='sitoshna'),
    
    
]

