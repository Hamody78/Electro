from django.shortcuts import render, redirect
from .forms import RegisterationForm
from .models import Account
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Verification Email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage, send_mail
from django.conf import settings

def register(request):
    if request.method == "POST":
        form = RegisterationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone_number = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()

            send_mail(
                "We Need You",
                "We Know that you are a engineer, and we need more engineers",
                email,
                [settings.EMAIL_HOST_USER]
            )

            messages.success(request, "Registration Successfully.")
            return redirect("register")
    else:
        form = RegisterationForm()


    context = {
        "form":form,
    }
    return render(request, "register.html", context)

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid Login Credentails.")
            return redirect("login")

    return render(request, "signin.html")

def dashboard(request):
    return render(request, "dashboard.html")

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, "Your are Logged out.")
    return redirect("login")

def activate(request):
    return