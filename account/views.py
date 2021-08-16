from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

#TODO: activate view, login view, logout view;


# 3 варианта для создания видов на классах: APIView, generic view, viewSet
class RegisterView(APIView):
    def post(self, request):
        data = request.data  # сейчас в переменной хранится querydict, данными, которые вводит пользователь
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return Response('Succesfully signed up!', status=status.HTTP_201_CREATED)
# TODO: а зачем мы передаем тут статус? то-есть для кого


class ActivateView(APIView):
    def get(self, request, activation_code):
        User = get_user_model()
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
