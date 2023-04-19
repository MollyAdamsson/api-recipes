from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Recipe model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    reviews_count = serializers.ReadOnlyField()
    average_rating = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        returns true if the user thats making the request
        is the owner of the recipe
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """
        Lists all of the fields that are included in
        the data returned by this API
        """
        model = Recipe
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'created_at', 'updated_at', 'reviews_count',
            'average_rating', 'description', 'ingredients', 'instructions', 
            'title'
            
        ]