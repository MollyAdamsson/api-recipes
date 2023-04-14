from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    """
    Recipe model, related to the users
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.owner}'s Recipe"