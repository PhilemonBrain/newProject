from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Home page view
def index(request):
    return render(request, 'homepage/index.html')


# About us view
def about(request):
    return render(request, 'homepage/about.html')


# Contact us page
def contact_us(request):
    """Sends an email to admin with user's data from the frontend"""
    if request.method == "POST":
        if request.POST.get("submit"):
            name = request.POST.get("name")
            email = request.POST.get("email")
            sender = settings.EMAIL_HOST_USER
            message = request.POST.get("message")
            admin = ""

            if name and email and message:
                send_mail(
                    email, message, name, [admin]
                )
    return render(request, 'homepage/contact.html')


# Views to FAQ
def faq(request):
    return render(request, 'homepage/faq.html')

#View to sign in
def signin(request):
    return render(request, 'accounts/sign_in.html')

#views to sign up
def signup(request):
    return render(request, 'accounts/sign_up.html')


#views to recover password
def recover_password(request):
    return render(request, 'accounts/recover_password.html')

#views to recover password
def reset_link(request):
    return render(request, 'accounts/reset_link_sent.html')

#views to recover password
def reset_password(request):
    return render(request, 'accounts/reset_password.html')
