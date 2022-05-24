from django.urls import path, include
from .views import *
from django.contrib import admin

urlpatterns = [
    # path('', post, name='post'),
    path('', board, name='board'),
    path('edit/<int:pk>', boardEdit, name='edit'),
    path('delete/<int:pk>', boardDelete, name='delete'),
    # path('admin/', admin.site.urls),
    # path('', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
]
