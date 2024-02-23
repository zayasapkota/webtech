from django.http import JsonResponse
from .models import Restaurant
from .serializers import RestaurantSerializer


def restaurant_detail(request):
    restaurant = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurant, many=True)
    return JsonResponse(serializer.data, safe=False)
