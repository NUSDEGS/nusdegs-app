from django.shortcuts import render
from django.http import JsonResponse

from .main import modsplanner

# Create your views here.

# To handle reques from the frontend

def get_plans_view(request):
    return JsonResponse(modsplanner(request))