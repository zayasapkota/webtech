from django.http import JsonResponse
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def restaurant_detail(request):
    restaurant = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurant, many=True)
    return JsonResponse(serializer.data, safe=False)

def stationcafe_view(request):
    # Your view logic goes here
    return render(request, 'stationcafe.html')  # Replace 'stationcafe.html' with your actual template name


def manjilcafe_view(request):
    # Your view logic goes here
    return render(request, 'manjilcafe.html')  # Replace 'stationcafe.html' with your actual template name


def bishalcafe_view(request):
    # Your view logic goes here
    return render(request, 'bishalcafe.html') 

def hungerkills_view(request):
    # Your view logic goes here
    return render(request, 'hungerkills.html') 

def janata_view(request):
    # Your view logic goes here
    return render(request, 'janata.html') 

def manakamanacafe_view(request):
    # Your view logic goes here
    return render(request, 'manakamanacafe.html') 

def matkacafe_view(request):
    # Your view logic goes here
    return render(request, 'matkacafe.html') 

def sarita_view(request):
    # Your view logic goes here
    return render(request, 'sarita.html') 

def sitoshna_view(request):
    # Your view logic goes here
    return render(request, 'sitoshna.html') 


from django.shortcuts import render

def stationcafe_view(request):
    return render(request, 'restaurants/stationcafe.html')

def manjilcafe_view(request):
    return render(request, 'restaurants/manjilcafe.html')

def bishalcafe_view(request):
    return render(request, 'restaurants/bishalcafe.html')

def hungerkills_view(request):
    return render(request, 'restaurants/hungerkills.html')

def janata_view(request):
    return render(request, 'restaurants/janata.html')

def manakamanacafe_view(request):
    return render(request, 'restaurants/manakamana.html')

def matkacafe_view(request):
    return render(request, 'restaurants/matkacafe.html')

def sarita_view(request):
    return render(request, 'restaurants/sarita.html')

def sitoshna_view(request):
    return render(request, 'restaurants/sitoshna.html')


def home_view(request):
    return render(request, 'index.html')
