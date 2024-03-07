from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def user_login(request):
    user = get_object_or_404(User, request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({
            "message": "Username or password not valid"
        }, status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    token, created = Token.objects.get_or_create(user=user)
    return Response({
        "token": token.key,
        "user": serializer.data
    })


@api_view(['POST'])
def user_signup(request):
    serializer = UserSerializer(data=request.data)
    if (serializer.is_valid()):
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.e
        user.save()
        token = Token.objects.create(user=user)
        return Response({
            "token": token.key,
            "user": serializer.data
        })
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def custom_login(request):
    # Custom login view implementation
    return render(request, 'accounts/login.html')  # Render login template


