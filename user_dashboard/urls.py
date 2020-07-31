from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.api_list, name='dashboard'),
    path('configure_api/', views.ConfigureApiView.as_view(), name='configure_api')
]