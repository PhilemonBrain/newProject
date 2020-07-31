from django.urls import path, re_path
from . import views
app_name = "user_dashboard"

urlpatterns = [
    path('', views.api_list, name='dashboard'),
    path('configure_api/', views.ConfigureApiView.as_view(), name='configure_api'),
    path('settings/', views.settings, name='settings')
]