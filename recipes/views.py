from django.db.models import Count, Avg
from rest_framework import generics, permissions, filters
from blog_api.permissions import IsOwnerOrReadOnly
from .models import Recipe
from .serializers import RecipeSerializer


class RecipeList(generics.ListCreateAPIView):
    """
    List recipes if logged in
    """
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Recipe.objects.all()

    filter_backends = [
        filters.SearchFilter
    ]

    search_fields = [
        'owner__username',
        'recipe',
        'ingredients',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecipeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a recipe, or update or delete it by id if you own it.
    """
    serializer_class = RecipeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Recipe.objects.all()