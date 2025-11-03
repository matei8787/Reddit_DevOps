from django.db import models
from django.contrib.auth.models import User
from bugs.models import Bug

# Create your models here.
class Vote(models.Model):
    UP = 1
    NOVOTE = 0
    DOWN = -1
    VOTE_CHOICES = [
        (UP, 'Upvote'),
        (DOWN, 'Downvote'),
        (NOVOTE, 'No Vote')
    ]
    
    made_by = models.OneToOneField(User, on_delete=models.CASCADE)
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    value = models.SmallIntegerField(choices=VOTE_CHOICES, default=NOVOTE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('made_by', 'bug')
        