from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from . models import ApiList, ActiveApiList
# Create your views here.

def api_list(request):
    all_apis = ApiList.objects.all()
    return render(request, 'user_dashboard/dashboard.html', {'all_apis':all_apis})


class ConfigureApiView(TemplateView):
    template_name = 'user_dashboard/configure_api.html'


