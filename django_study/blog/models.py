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
