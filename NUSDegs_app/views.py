from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .main import modsplanner

# Create your views here.

# To handle reques from the frontend

@csrf_exempt
def get_plans_view(request):
    return JsonResponse(modsplanner(request.body))