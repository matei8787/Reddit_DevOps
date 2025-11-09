from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer
from core.util import get_token
from django.shortcuts import render
from .forms import LoginForm, RegisterForm
import logging
from django_ratelimit.decorators import ratelimit
logger = logging.getLogger('auth_logger')


@api_view(['POST'])
@ratelimit(key='ip', rate='3/m', block=True)
def register_api(req):
    logger.info(f"{datetime.now()}: Registration attempt with username: {req.data.get('username', 'unknown')}")
    serializer = RegisterSerializer(data=req.data)
    if serializer.is_valid():
        user = serializer.save()
        logger.info(f"{datetime.now()}: User registered successfully: {user.username}")
        return Response({'success': True}, status=status.HTTP_201_CREATED)
    logger.warning(f"{datetime.now()}: Registration failed: {serializer.errors}")
    return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@ratelimit(key='ip', rate='6/m', block=True)
def login_api(req):
    logger.info(f"{datetime.now()}: Login attempt with username: {req.data.get('username', 'unknown')}")
    serializer = LoginSerializer(data=req.data)
    if serializer.is_valid():
        token = serializer.validated_data['token']
        logger.info(f"{datetime.now()}: User logged in successfully: {req.data.get('username', 'unknown')}")
        return Response({'success': True,
                         'access': token['access'],
                         'refresh': token['refresh']}, status=status.HTTP_200_OK)
    logger.warning(f"{datetime.now()}: Login failed: {serializer.errors}")
    return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

def login_view(req):
    if req.method == 'POST':
        return HttpResponse("Login via API.")
    return render(req, 'login.html', {
        'form': LoginForm()
    })
    
def register_view(req):
    if req.method == 'POST':
        return HttpResponse("Register via API.")
    return render(req, 'register.html', {
        'form': RegisterForm()
    })