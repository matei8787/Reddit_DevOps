from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer
from .util import get_token
from django.shortcuts import render
from .forms import LoginForm, RegisterForm

@api_view(['POST'])
def register_api(req):
    serializer = RegisterSerializer(data=req.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'success': True}, status=status.HTTP_201_CREATED)
    return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_api(req):
    serializer = LoginSerializer(data=req.data)
    if serializer.is_valid():
        token = serializer.validated_data['token']
        return Response({'success': True,
                         'access': token['access'],
                         'refresh': token['refresh']}, status=status.HTTP_200_OK)
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