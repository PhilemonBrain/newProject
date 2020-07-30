from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


# Home page view
class HomeView(TemplateView):
    template_name = "homepage/index.html"


# About us view
def about(request):
    return render(request, 'homepage/about.html')


# Contact us page
def contact_us(request):
    context = {}
    return render(request, 'homepage/contact.html', context)


# Views to FAQ
def faq(request):
    return render(request, 'homepage/faq.html')

