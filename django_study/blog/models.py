from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)  # 글자수 제한이 있을때
    text = models.TextField()  # 글자수 제한이 없을때

    def __str__(self):
        return self.text


class Board(models.Model):
    title = models.CharField(max_length=20, null=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)


###### movie models ######

class Movie_info(models.Model):
    code_id = models.IntegerField(blank=False)
    title = models.CharField(max_length=50)
    actual_score = models.IntegerField(blank=False)
    spc_score = models.IntegerField(blank=False)
    net_score = models.IntegerField(blank=False)
    running_time = models.IntegerField(blank=False)

    def __str__(self):
        return self.title


class Country(models.Model):
    _id = models.ForeignKey(Movie_info, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=20)


class Actor(models.Model):
    _id = models.ForeignKey(Movie_info, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)


class Director(models.Model):
    _id = models.ForeignKey(Movie_info, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)


class Genre(models.Model):
    # _id = models.ManyToManyField(Movie_info)
    movie_id = models.ForeignKey(
        Movie_info, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=30)


# class Movie_genre(models.Model):
    # code_id = models.ForeignKey(Movie_info, on_delete=models.CASCADE)
    # _id = models.ForeignKey(Genre, on_delete=models.CASCADE)
