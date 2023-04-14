from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model, related to owner that is the user following another user.
    The related_name attribute seperates  'owner' and 'followed'.
    'unique_togetehr' makes sure that you cant follow someone twice.
    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'