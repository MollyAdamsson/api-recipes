from django.db import IntegrityError
from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    """
    The serializer for the like model
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    

    class Meta:
        model = Rating
        fields = [
            "id",
            "owner",
            "post",
            "user_rating",
            "created_at",
    ]

    def create(self, validate_data):
        try:
            return super().create(validate_data)
        except IntegrityError:
            raise serializers.validationError({
                ''
            })