from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'login.html', {'error': 'Passwords do not match'})

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'login.html', {'error': 'Username already exists'})

        # Create the user
        print(username)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        print('user created')
        return redirect('login')  # Redirect to the login page
    else:
        return render(request, 'login.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print('user logged in ')
            return redirect('index')  # Redirect to the index page after successful login
        else:
            print('invalid user')
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        print('invalid method')
        return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')
