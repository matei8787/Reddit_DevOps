from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from bugs.models import Bug
from .models import Vote
import logging
from django_ratelimit.decorators import ratelimit
from datetime import datetime
logger = logging.getLogger('votes_logger')

# Create your views here.
@api_view(['POST'])
@ratelimit(key='ip', rate='30/m', block=True)
@permission_classes([IsAuthenticated])
def upvote_view(req, bug_id):
    bug = Bug.objects.filter(id=bug_id).first()
    if not bug:
        return Response({'error': 'Bug not found.'}, status=status.HTTP_404_NOT_FOUND)
    user = req.user
    vote, created = Vote.objects.get_or_create(made_by=user, bug=bug)
    vote.value = Vote.UP
    vote.save()
    logger.info(f"{datetime.now()}: User {user.username} upvoted bug {bug.id}.")
    return Response({'message': 'Bug upvoted successfully.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@ratelimit(key='ip', rate='30/m', block=True)
def downvote_view(req, bug_id):
    bug = Bug.objects.filter(id=bug_id).first()
    if not bug:
        return Response({'error': 'Bug not found.'}, status=status.HTTP_404_NOT_FOUND)
    user = req.user
    vote, created = Vote.objects.get_or_create(made_by=user, bug=bug)
    vote.value = Vote.DOWN
    vote.save()
    logger.info(f"{datetime.now()}: User {user.username} downvoted bug {bug.id}.")
    return Response({'message': 'Bug downvoted successfully.'}, status=status.HTTP_200_OK)