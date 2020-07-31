from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from  django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
import requests
from .models import User

# Create your views here.

#this is the login page
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        print(request.POST)
        user = auth.authenticate(email=email, password=password, username=username)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard:dashboard")
        else:
            messages.info(request, 'invalid credentials')
            return redirect("accounts:signin")
    return render(request,"accounts/sign_in.html")

def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        confirm_pass = request.POST.get('confirmpwd')
        password = request.POST.get('pwd')
        print(request.POST)
        if password == confirm_pass:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Username Taken, Please try again')
                return redirect('signup')
                print(User.objects.all(), 1)
                
            else:
                url = "https://auth-microapi.herokuapp.com/api/user/register"
                payload = {
                    "username":username,
                    "email": email,
                    "password": password,
                    "phone_number": phonenumber,
                }
                headers= {
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVmMjJmY2QxYTUwOTA4MDAwNGQ5MmVlMSIsImVtYWlsIjoidWphbWVzNDFAeWFob28uY29tIiwiREJVUkkiOiJtb25nb2RiK3NydjovL2Z1bGxzdGFjazpmdWxsc3RhY2tAc2FuZGJveC0xbG00aC5tb25nb2RiLm5ldC9hdXRoLWFwcD9yZXRyeVdyaXRlcz10cnVlIiwiaWF0IjoxNTk2MTMzODMyfQ.Hj4qWdwl7F-nDsI76noGLMo-hz0uZphntLMjG-SPMQs"
                }
                # response = requests.request("POST", url, headers=headers, data = payload)
                response = requests.request("POST", url, headers=headers, data= payload)

                response = response.json()
                print(response)
                if response['success'] == True:

                    user = User(username=response['data']['username'])
                    print(user)
                    user.email = response['data']['email']
                    user.user_id = response['data']['id']
                    user.is_active = False
                    user.save()
                    msg =response['message']
                    messages.info(request, f'{msg}')
                    return redirect("accounts:signin")
                else:
                    msg =response['message']
                    messages.info(request, f'{msg}')
                    return redirect("accounts:signup") 
                print(User.objects.all(), 3)
        else:
            messages.error(request, 'Password mismatch')
            return redirect("accounts:signup")       
    return render(request, "accounts/sign_up.html")