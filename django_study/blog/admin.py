from .models import *
from . import models
from django.contrib import admin
# from .models import Movie_info, Post
import logging
# 로그 생성
logger = logging.getLogger()
# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)
# log 출력 형식
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# Register your models here.


@admin.register(Post)
class PostAmdin(admin.ModelAdmin):
    list_display = ['title']
    list_link = ['title']


class containMovie(admin.StackedInline):
    model = Genre
    extra = 0


@admin.register(Movie_info)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_gerne']
    list_link = ['title']

    inlines = [containMovie, ]

    def get_gerne(self, obj):
        logger.info(f"""{Genre.objects.filter(id=obj.id).values_list()}""")
        return list(Genre.objects.filter(id=obj.id).values_list())

        # return obj
