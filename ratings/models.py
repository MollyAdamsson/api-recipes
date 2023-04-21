from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Rating(models.Model):
    """
    Ratings model, connected to the owner and makes it possible for other users 
    to rate eachothers posts
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='ratings', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(blank=True, null=True)


    class Meta:
        ordering = ["-created_at"]
        unique_together = [['owner', 'post']]
    
    def __str__(self):
        return f"{self.owner} {self.post}"