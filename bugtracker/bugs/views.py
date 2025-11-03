from django.shortcuts import render
from .models import Bug
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BugSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .forms import BugForm

def index(req):
    bugs = Bug.objects.all()
    form = BugForm()
    return render(req, 'index.html', {'bugs': bugs, 'form': form})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_bug(req):
    serializer = BugSerializer(data=req.data, context={'request': req})
    if serializer.is_valid():
        bug = serializer.save()
        return Response({**BugSerializer(bug).data, 'success': True}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_bug(req, bug_id):
    bug = Bug.objects.filter(id=bug_id).first()
    if not bug:
        return Response({'error': 'Bug not found.'}, status=status.HTTP_404_NOT_FOUND)
    serializer = BugSerializer(bug)
    return Response(serializer.data, status=status.HTTP_200_OK)

def view_bug(req, bug_id):
    bug = Bug.objects.filter(id=bug_id).first()
    if not bug:
        return render(req, '404.html', status=404)
    return render(req, 'view_bug.html', {'bug': bug})