from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import CommentNRatingSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_comment_rating(request):
    serializer = CommentNRatingSerializer(data=request.data)
    if (serializer.is_valid()):
        serializer.save()
        return Response({
            "data": serializer.data
        })
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
