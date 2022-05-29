from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('blog.urls')),
    # path('accounts/', include('accounts.urls')),
    # path('signup/', signup, name='signup'),
    # path('signup3/', signup3, name='signup3'),
    path('home/signup/', signup, name='signup'),
    path('home/login/', login, name='login'),
    path('home/logout/', logout, name='logout'),
    path('home/', home, name='home'),
]
