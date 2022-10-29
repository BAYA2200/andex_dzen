from django.db import models

# Create your models here.
from account.models import Author


class Post(models.Model):
    text = models.CharField(max_length=100)
    created = models.DateTimeField(max_length=1, auto_now_add=True, default=1)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Rating(models.Model):
    score_post = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    score = models.ForeignKey(Post, choices=score_post, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
