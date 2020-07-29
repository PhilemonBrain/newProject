from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . models import apiBox
# Create your views here.

class DashboardView(ListView):
    template_name = "user_dashboard/dashboard.html"
    model = apiBox

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['queryset'] = apiBox.objects.all()
        return context

class ConfigureApiView(TemplateView):
    template_name = 'user_dashboard/configure_api.html'