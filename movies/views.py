from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'movies/home.html')

def register(request):
    return redirect('register')