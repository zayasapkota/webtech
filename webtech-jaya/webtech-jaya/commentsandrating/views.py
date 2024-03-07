from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import CommentNRating
from .serializers import CommentNRatingSerializer
from rest_framework.response import Response

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_comment_rating(request):
    serializer = CommentNRatingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response({"data": serializer.data})
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class RestaurantComments(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = CommentNRatingSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs['restaurant_id']
        return CommentNRating.objects.filter(restaurant_id=restaurant_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"data": serializer.data})