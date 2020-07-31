from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.conf import settings
import requests
from .models import User


class ApiAuthBackend(BaseBackend):
    """
    Authenticate User against the email auth
    """
    print('yeah')

    def authenticate(self, request, **kwargs):
        email = kwargs['email']
        password = kwargs['password']
        print(email, password)

        if email and password:
            try:
                endpoint = '{api_url}user/login'
                url = endpoint.format(api_url=settings.AUTH_API_URL)

                payload = {
                    "password": password,
                    "email": email,
                }
                # set Authorization header
                headers = {
                    "Authorization": "Bearer %s" % (settings.AUTH_ADMIN_TOKEN)
                }

                # response = requests.get(url, headers=headers, data = payload)
                response = requests.request(
                    "POST", url, headers=headers, data=payload)
                response = response.json()
                print(response['data'])

                if response['success'] == True:
                    user = get_user_model().objects.get(email=email)
                    print(user)
                    return user
            except get_user_model().DoesNotExist:
                return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
