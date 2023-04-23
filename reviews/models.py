from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile

class Review(models.Model):
    """
    Model for the reviews
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    profiles = models.ForeignKey(
        Profile, related_name='profiles', on_delete=models.CASCADE
    )
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner}'s review"