from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    template_name = "accounts/index.html"
    args = {}
    return render(request,template_name,args)
