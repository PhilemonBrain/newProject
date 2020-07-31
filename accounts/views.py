from django.shortcuts import render
# import conf from settings
from django.conf import settings
#import http
from django.http import HttpResponse
# import requests for http requests
import requests
#import json
import json

# Create your views here.

# signin function


def signin(request):
    if request.method == "POST":
        endpoint = '{api_url}user/login'
        url = endpoint.format(api_url=settings.AUTH_API_URL)
        token = 'Bearer %s' % (settings.AUTH_ADMIN_TOKEN)
        payload = {"email": request.POST["email"],
                   "password": request.POST["password"]}
        headers = {'Authorization': '%s' % (token)}
        # make http call to endpoint
        response = requests.post(url, data=payload, headers=headers)

        if response.status_code == 200:
            result = response.json()
            session_data = {"username": result["data"]["data"]["username"],
                            "email": result["data"]["data"]["email"], "userId": result["data"]["data"]["id"]}
            request.sessions = session_data

            print(result["data"]["data"]["username"])
            return HttpResponse("Login Successful. Redirecting to dashboard ...")
