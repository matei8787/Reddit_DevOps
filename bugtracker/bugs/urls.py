from django.urls import path, include
from .views import index, create_bug, get_bug, view_bug
urlpatterns = [
    path('', index, name='index'),
    path('api/create', create_bug, name='create_bug'),
    path('api/<int:bug_id>/', get_bug, name='get_bug'),
    path('<int:bug_id>/', view_bug, name='view_bug'),
]
