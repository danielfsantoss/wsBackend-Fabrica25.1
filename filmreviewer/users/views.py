from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .api.serializer import UserSerializer

import json

# Create your views here.

def register(request):
    return render(request, '')
