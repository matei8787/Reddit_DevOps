from django.shortcuts import render
from .models import Bug
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BugSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .forms import BugForm
import logging
from datetime import datetime
from django_ratelimit.decorators import ratelimit

logger = logging.getLogger('bugs_logger')

def index(req):
    bugs = Bug.objects.all()
    form = BugForm()
    return render(req, 'index.html', {'bugs': bugs, 'form': form})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@ratelimit(key='ip', rate='8/m', block=True)
def create_bug(req):
    logger.info(f"{datetime.now()}: User: {req.user.username} is creating a bug.")
    serializer = BugSerializer(data=req.data, context={'request': req})
    if serializer.is_valid():
        bug = serializer.save()
        logger.info(f"{datetime.now()}: Bug {bug.id} created successfully by: {req.user.username}.")
        return Response({**BugSerializer(bug).data, 'success': True}, status=status.HTTP_201_CREATED)
    logger.warning(f"{datetime.now()}: Bug creation failed: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@ratelimit(key='ip', rate='20/m', block=True)
def get_bug(req, bug_id):
    bug = Bug.objects.filter(id=bug_id).first()
    if not bug:
        return Response({'error': 'Bug not found.'}, status=status.HTTP_404_NOT_FOUND)
    serializer = BugSerializer(bug)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def view_bug(req, bug_id):
    bug = Bug.objects.filter(id=bug_id).first()
    if not bug:
        return render(req, '404.html', status=404)
    return render(req, 'view_bug.html', {'bug': bug})