from rest_framework import generics, permissions, filters
from blog_api.permissions import IsOwnerOrReadOnly
from .models import ProfileReview
from .serializers import ProfileReviewSerializer, ProfileReviewDetailSerializer


class ProfileReviewList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = ProfileReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = ProfileReview.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfileReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileReviewDetailSerializer
    queryset = ProfileReview.objects.all()