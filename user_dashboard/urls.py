from django.urls import path
from .views import ConfigureApiView, ApiView

urlpatterns = [
    path('', ApiView.as_view(), name='dashboard'),
    path('configure_api/', ConfigureApiView.as_view(), name='configure_api')
]