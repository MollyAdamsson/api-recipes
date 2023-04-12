from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    The serializer for the comments model
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Returns true if the user is the creator of the comment
        """
        request = self.context["request"]
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        Returns a time when it was created
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Returns the time the
        comment was updated
        """
        return naturaltime(obj.updated_at)

    class Meta:
        """
        List of the different fields
        """
        model = Comment
        fields = [
            "id",
            "owner",
            'post',
            "is_owner",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
            "content",
        ]

class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    post = serializers.ReadOnlyField(source="post.id")