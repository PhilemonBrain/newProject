from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "accounts"


urlpatterns = [
    path('login/', views.login, name='signin'),
    path('signup/', views.register, name='signup'),
]