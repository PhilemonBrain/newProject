from django.urls import path
from .views import DashboardView, ConfigureApiView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('configure_api/', ConfigureApiView.as_view(), name='configure_api')
]