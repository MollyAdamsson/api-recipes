from rest_framework import serializers
from posts.models import Post


class PostSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        """
        Validates the size and height of images
        and sends a message if file is too large to upload
        """
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

    
    class Meta:
        model = Post
        fields = [
        'id', 'owner', 'is_owner', 'profile_id', 'profile_image', 'created_at',
        'updated_at', 'title', 'content', 'image', 'image_filter', 'rating', 
        ]
