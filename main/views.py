from django.shortcuts import render
from django.http import HttpResponse
from .models import assets 

def index(request):
    asset = assets.objects.all()
    return render(request, "index.html", {"asset":asset})

