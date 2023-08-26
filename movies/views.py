from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import post, Movie
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    movies = Movie.objects.all()
    return render(request, 'movies/home.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie_obj = get_object_or_404(Movie, pk=movie_id)
    # if(movie_obj.title=='spider-man'):
    #     print('true')
    comments = post.objects.filter(movie=movie_obj)
    # print(comments)
    return render(request, 'movies/movie_detail.html', {'movie': movie_obj, 'comments': comments})

class PostDetailView(DetailView):
    model = post

class PostListView(DetailView):
    model = post
    template_name = 'movies/movie_detail.html'
    context_object_name = 'post'
    ordering = ['-date_posted']

class PostCreateView(LoginRequiredMixin, CreateView):
    model = post
    fields = ['rating', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        movie_pk = self.request.POST.get('movie')
        movie_obj = get_object_or_404(Movie, pk=movie_pk)
        form.instance.movie = movie_obj
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        print(request.POST.get('movie'))  # Add this line
        return super().post(request, *args, **kwargs)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = post
    fields = ['rating', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def movie(request):
    context = {
        'posts': post.objects.all()
    }
    return render(request, 'movies/movie_detail.html', context)
