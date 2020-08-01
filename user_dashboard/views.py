from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from . models import ApiList, ActiveApiList, Project
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from homepage.views import index
import uuid

@login_required(login_url='/accounts/signin')
def api_list(request, id):
    user = request.user
    project = Project.objects.get(id=id)
    # project = Project.objects.filter(user_id=user.id).filter(name='project1').first()
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


def adding_api(request, id):
    add_to_api = ApiList.objects.get(id=id)
    user = request.user
    print(user)
    User.add_api(api = add_to_api, name = user)
    #all_apis = ApiList.objects.order_by('title')
    return redirect('/dashboard')
    #return render(request, 'user_dashboard/dashboard.html', {'all_apis':all_apis})

def rmv_api(request, id):
    add_to_api = ApiList.objects.get(id=id)
    user = request.user
    user.api_list.remove(add_to_api)
    return redirect('/dashboard')


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
    if request.method ==  "POST":

        project_name = request.POST['project_name']
        user = request.user
        project = Project.objects.filter(user_id=user.id).filter(name=project_name) #user.id or user.user_id??
        print(project)
        if not project:
            proj = Project.objects.create(
                name = project_name,
                user_id = user,
                token = uuid.uuid4().hex
            )
            proj.save()
            print(proj)
            projID = proj.id
            print("done creating")
            return redirect("dashboard:dashboard", id=(projID))
        else:
            return redirect('/dashboard')



@login_required(login_url='/accounts/signin')
def switch(request, project_name):
    user = User.objects.all()
    all_apis = ApiList.objects.all()
    return render(request, 'user_dashboard/switch_project.html', {'all_apis':all_apis})