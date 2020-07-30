from django.urls import path
from . import views


urlpatterns = [
    path('docs/comment_api', views.docs, name="docs"),
    path('docs/auth_api', views.docs, name="authdocs"),
    path('docs/consultant', views.consultant, name="consultant")
]