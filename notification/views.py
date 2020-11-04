from django.shortcuts import render, redirect
from .models import *
import secrets
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render("home.html")