from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.conf import settings
import requests
from .models import User


class ApiAuthBackend(BaseBackend):
    """
    Authenticate User against the email auth
    """

    def authenticate(self, request, **kwargs):
        email = kwargs['email']
        password = kwargs['password']

        if email and password:
            try:
                #endpoint = '{api_url}user/login'
                url = 'https://auth-microapi.herokuapp.com/api/user/login'

                payload = {
                    "password": password,
                    "email": email,
                }
                # set Authorization header
                headers = {
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVmMjMzNzE2NGM1NjRkMDAwNDBlZDllNyIsImVtYWlsIjoiaWNlYmVla2F5eUBnbWFpbC5jb20iLCJEQlVSSSI6Im1vbmdvZGIrc3J2Oi8vZnVsbHN0YWNrOmZ1bGxzdGFja0BzYW5kYm94LTFsbTRoLm1vbmdvZGIubmV0L2F1dGgtYXBwP3JldHJ5V3JpdGVzPXRydWUiLCJpYXQiOjE1OTYxNDM0NDd9.E_zJqUcM8s0RHKamaE-gQss9Y1F1Nn0TRSu3q_45E58"
                }

                # response = requests.get(url, headers=headers, data = payload)
                response = requests.request(
                    "POST", url, headers=headers, data=payload)
                response = response.json()

                if response['success'] == True:
                    user = get_user_model().objects.get(email=email)
                    return user
            except get_user_model().DoesNotExist:
                return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
