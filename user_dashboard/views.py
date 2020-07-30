from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . models import ApiList
# Create your views here.

class ApiView(TemplateView):
    template_name = "user_dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(ApiView, self).get_context_data(**kwargs)
        context['api_lists'] = ApiList.objects.all()
        return context

class ConfigureApiView(TemplateView):
    template_name = 'user_dashboard/configure_api.html'