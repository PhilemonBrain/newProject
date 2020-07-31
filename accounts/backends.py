from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
import requests

class ApiAuthBackend(BaseBackend):
    """
    Authenticate User against the email auth
    """
    print('yeah')
    def authenticate(self, request, **kwargs):
        email = kwargs['email']
        username = kwargs['username']
        password = kwargs['password']
        print(email,password)

        if email and password:
            try:
                url = "https://auth-microapi.herokuapp.com/api/user/login"

                # payload = "{\r\n\"username\":\"%s\",\r\n\"email\":\"%s\"\r\n\r\n} " % (username,email)
                # payload = ""
                payload = {
                    "password":password,
                    "email": email,
                }

                # API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVmMjJmY2QxYTUwOTA4MDAwNGQ5MmVlMSIsImVtYWlsIjoidWphbWVzNDFAeWFob28uY29tIiwiREJVUkkiOiJtb25nb2RiK3NydjovL2Z1bGxzdGFjazpmdWxsc3RhY2tAc2FuZGJveC0xbG00aC5tb25nb2RiLm5ldC9hdXRoLWFwcD9yZXRyeVdyaXRlcz10cnVlIiwiaWF0IjoxNTk2MTMzODMyfQ.Hj4qWdwl7F-nDsI76noGLMo-hz0uZphntLMjG-SPMQs"
                headers= {
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVmMjJmY2QxYTUwOTA4MDAwNGQ5MmVlMSIsImVtYWlsIjoidWphbWVzNDFAeWFob28uY29tIiwiREJVUkkiOiJtb25nb2RiK3NydjovL2Z1bGxzdGFjazpmdWxsc3RhY2tAc2FuZGJveC0xbG00aC5tb25nb2RiLm5ldC9hdXRoLWFwcD9yZXRyeVdyaXRlcz10cnVlIiwiaWF0IjoxNTk2MTMzODMyfQ.Hj4qWdwl7F-nDsI76noGLMo-hz0uZphntLMjG-SPMQs"
                }

                # response = requests.get(url, headers=headers, data = payload)
                response = requests.request("POST", url, headers=headers, data= payload)
                response = response.json()
                print(response['data'])

                if response['success'] == True and response['data']['data']['isEmailVerified'] == True:
                    
                    user = get_user_model().objects.get(email=email) 
                    print(user)
                    return user
            except get_user_model().DoesNotExist:
                return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None