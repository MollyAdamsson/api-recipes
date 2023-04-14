from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    The serializer for the like model
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    

    class Meta:
        model = Like
        fields = [
            "id",
            "owner",
            "post",
            "created_at",
    ]

    def create(self, validate_data):
        try:
            return super().create(validate_data)
        except IntegrityError:
            raise serializers.validationError({
                'detail': 'possible duplicate'
            })