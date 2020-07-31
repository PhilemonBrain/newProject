from django.shortcuts import render
# import conf from settings
from django.conf import settings
# import requests for http requests
import requests
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
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
            print (result)
