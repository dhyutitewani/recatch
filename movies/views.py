from django.shortcuts import render, redirect
from .models import post

# Create your views here.
def home(request):
    return render(request, 'movies/home.html')

def movie(request):
    context = {
        'posts': post.objects.all()
    }
    return render(request, 'movies/movie.html', context)
