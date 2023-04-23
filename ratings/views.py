from rest_framework import generics, permissions
from blog_api.permissions import IsOwnerOrReadOnly
from .models import Rating
from .serializers import RatingSerializer


class RatingList(generics.ListCreateAPIView):
    """
    This list the ratings and makes it possible to create a rating
    only if the user is logged in
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

    def perform_create(self, serializer):
        """
        Passes the user as the owner when a rating is created
        """
        serializer.save(owner=self.request.user)


class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a rating
    """
    serializer_class = RatingSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Rating.objects.all()