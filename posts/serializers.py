from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from ratings.models import Rating


class PostSerializer(serializers.ModelSerializer):
    """
    The serializer for the post model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    rating_id = serializers.SerializerMethodField()
    ratings_count = serializers.ReadOnlyField()
    user_rating = serializers.SerializerMethodField()
    total_stars = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 4 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 4MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_rating_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            rating = Rating.objects.filter(
                owner=user, post=obj
            ).first()
            return rating.id if rating else None
        return None

    def get_user_rating(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            rating = Rating.objects.filter(
                owner=user, post=obj
            ).first()
            return rating.user_rating if rating else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter',
            'like_id', 'likes_count', 'comments_count', 'rating_id', 'user_rating',
            'ratings_count', 'total_stars', 'ingredients',
            'instructions',
        ]
