from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Users
from .api.serializer import UsersSerializer

# import requests

import json

OMDB_API_KEY = '6e7e7f5d'

@api_view(['POST'])
def create_user(request):
    serializer = UsersSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def create_review(request):
  return HttpResponse(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(['GET'])
def get_reviews(request):
  return HttpResponse(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(['GET'])
def get_review_by_id(request):
  return HttpResponse(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(['PATCH'])
def update_review(request):
  return HttpResponse(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(['DELETE'])
def delete_review(request):
  return HttpResponse(status=status.HTTP_501_NOT_IMPLEMENTED)


# def get_movie(movie_title):
#   omdb_url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
#   response = requests.get(omdb_url)
#   movie_data = response.json()
#   return movie_data.get('Title')