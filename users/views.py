from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserLoginForm

import pyrebase as firebase

firebaseConfig = {
    "apiKey": "AIzaSyAGy2iRgkPP_PVOFYiAfESLgYb_eLrT6eU",
    "authDomain": "django-3aca5.firebaseapp.com",
    "projectId": "django-3aca5",
    "storageBucket": "django-3aca5.appspot.com",
    "messagingSenderId": "212972838840",
    "appId": "1:212972838840:web:ff68185a3545e5628e394d",
    "measurementId": "G-WGEYCC1HFJ",
    "databaseURL": "",
}

app = firebase.initialize_app(firebaseConfig)
authenticate_user = app.auth()

class UserLogin(LoginView):
    authentication_form = UserLoginForm
    template_name = 'users/login.html'

def signup_view(request):

    return render(request, 'users/signup.html')

def homepage_view(request):

    return render(request, 'user/homepage.html')