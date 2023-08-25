from django.shortcuts import render, redirect
from .models import post

posts = [
    {
        'author': 'abc',
        'title': 'movie title',
        'review': 'good/bad',
        'content': 'movie content',
        'date_posted': 'August 27, 2018'
    }
]

# Create your views here.
def home(request):
    return render(request, 'movies/home.html')

def movie(request):
    context = {
        'posts': posts
    }
    return render(request, 'movies/movie.html', context)

# def register(request):
#     return redirect('register')