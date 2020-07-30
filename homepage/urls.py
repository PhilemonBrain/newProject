from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    path('about/', views.about, name="about"),
    path('contact_us/', views.contact_us, name="contact"),
    path('faq/', views.faq, name="faq"),
    path('signin/',views.signin, name="signin"),
    path('docs/', views.docs, name="docs")
]