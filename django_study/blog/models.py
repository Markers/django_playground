from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)  #글자수 제한이 있을때
    text = models.TextField()  #글자수 제한이 없을때

    def __str__(self):
        return self.title
