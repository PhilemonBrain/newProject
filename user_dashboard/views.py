from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from . models import ApiList, ActiveApiList, Project
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from homepage.views import index

@login_required(login_url='/accounts/signin')
def api_list(request):
    user = request.user
    project = Project.objects.filter(user_id=user.id).filter(name='project1').first()
    print(project)
    active_api = ActiveApiList.objects.filter(project=project)
    print(active_api)
    all_apis = ApiList.objects.order_by('title')
    print(all_apis)
    context = {
        'active_api':active_api,
        'all_apis':all_apis
    }
    return render(request, 'user_dashboard/dashboard.html', context)


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


@login_required(login_url='/accounts/signin')
def addProject(request):
    project_name = "project5"
    user = request.user
    project = Project.objects.filter(user_id=user.id).filter(name=project_name) #user.id or user.user_id??
    print(project)
    if not project:
        Project.objects.create(
            name = project_name,
            user_id = user
            # token = token
        )
        # context = {
        #     'project':project_name,
        # }
        print("done creating")
        return HttpResponseRedirect(reverse('api_list'))



@login_required(login_url='/accounts/signin')
def switch(request, project_name):
    user = User.objects.all()
    all_apis = ApiList.objects.all()
    return render(request, 'user_dashboard/switch_project.html', {'all_apis':all_apis})