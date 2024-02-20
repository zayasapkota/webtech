from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Comment, Rating
from .forms import CommentForm, RatingForm

@login_required
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('restaurant_detail', restaurant_id=comment.restaurant.id)
    else:
        form = CommentForm()
    return render(request, 'commentsandrating/add_comment.html', {'form': form})

@login_required
def add_rating(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.save()
            return redirect('restaurant_detail', restaurant_id=rating.restaurant.id)
    else:
        form = RatingForm()
    return render(request, 'commentsandrating/add_rating.html', {'form': form})

# Define more views as needed for listing comments, ratings, etc.
