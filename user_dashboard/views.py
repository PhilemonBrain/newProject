from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from . models import ApiList, ActiveApiList
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from homepage.views import index

@login_required(login_url='/accounts/signin')
def api_list(request):
    user = User.objects.all()
    all_apis = ApiList.objects.order_by('title')
    return render(request, 'user_dashboard/dashboard.html', {'all_apis':all_apis})


def active_api(request, user, id):
    if request.method == 'POST':
        all_api = request.POST['all_api']
    return render(request, 'user_dashboard/dashboard.html', {'added_apis':added_apis})


@login_required(login_url='/accounts/signin')
def configure_api(request):
    return render(request, 'user_dashboard/configure_api.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def settings(request):
    return render(request, 'user_dashboard/acct_settings.html')


