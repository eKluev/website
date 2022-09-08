from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from . import settings

urlpatterns = [
    path('ap/', admin.site.urls),
    path('', include('main.urls')),
]
