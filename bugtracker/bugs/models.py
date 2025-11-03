from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bug(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    @property
    def score(self):
        from votes.models import Vote
        votes = Vote.objects.filter(bug=self)
        return sum(vote.value for vote in votes)

    @property
    def upvotes(self):
        from votes.models import Vote
        return Vote.objects.filter(bug=self, value=Vote.UP).count()
    @property
    def downvotes(self):
        from votes.models import Vote
        return Vote.objects.filter(bug=self, value=Vote.DOWN).count()