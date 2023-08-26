from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class post(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.TextField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Post for {self.movie.title} by {self.author.username}"

    def get_absolute_url(self):
        return reverse('movies-movie', kwargs={'movie_id': self.movie.pk})
