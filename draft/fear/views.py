from django.shortcuts import render
from django.http import HttpResponse
from .models import Champions
# Create your views here.

def index(request):
    champion_list = Champions.objects.order_by('champion_name')
    output = ', '.join([c.champion_name for c in champion_list])
    return HttpResponse(output)

def detail(request, champion_name):
    return HttpResponse("It is %s"%champion_name)
