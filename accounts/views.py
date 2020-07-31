from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
from django.conf import settings
import requests
import json
from .models import User


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(request.POST)
        user = auth.authenticate(email=email, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard:dashboard")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect("accounts:signin")
    return render(request, "accounts/sign_in.html")


def signup(request):

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
                messages.info(request, 'Username Taken, Please try again')
                return redirect('signup')
                print(User.objects.all(), 1)

            else:
                endpoint = '{api_url}user/register'
                url = endpoint.format(api_url=settings.AUTH_API_URL)
                payload = {
                    "username": username,
                    "email": email,
                    "password": password,
                    "phone_number": phonenumber,
                }
                headers = {
                    "Authorization": "Bearer %s" % (settings.AUTH_ADMIN_TOKEN)
                }
                # response = requests.request("POST", url, headers=headers, data = payload)
                response = requests.request(
                    "POST", url, headers=headers, data=payload)

                response = response.json()
                print(response)
                if response['success'] == True:

                    user = User(username=response['data']['username'])
                    print(user)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.email = response['data']['email']
                    user.user_id = response['data']['id']
                    user.is_active = False
                    user.save()
                    msg = response['message']
                    messages.info(request, f'{msg}')
                    return redirect("accounts:signin")
                else:
                    msg = response['message']
                    messages.info(request, f'{msg}')
                    return redirect("accounts:signup")
                print(User.objects.all(), 3)
        else:
            messages.error(request, 'Password mismatch')
            return redirect("accounts:signup")
    return render(request, "accounts/sign_up.html")
