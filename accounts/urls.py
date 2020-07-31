from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('login/', views.login, name='signin'),
    path('signup/', views.register, name='signup'),
]
