from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView
from . import views

urlpatterns = [
    path('', views.home, name='movies-home'),
    path('post/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostDetailView.as_view(), name='post-update'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movies-movie'),
]