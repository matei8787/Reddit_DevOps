from django.urls import path
from .views import upvote_view, downvote_view

urlpatterns = [
    path('<int:bug_id>/upvote/', upvote_view, name='upvote'),
    path('<int:bug_id>/downvote/', downvote_view, name='downvote'),
]