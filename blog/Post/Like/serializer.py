from rest_framework import serializers

from Post.models import Post

from .models import Like
from Users.models import Users


class CreateLikeSer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

    def create(self, validated_data):
        like = Like.objects.create(**validated_data)
        if validated_data["post"]:
            user = Users.objects.get(pk=validated_data["user"].id)
            post = Post.objects.get(pk=validated_data["post"].id)
            tags = post.tags.all()
            for tag in tags:
                user.recommendation.add(tag.id)
        like.save()
        return like


class GetLikeSer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

    def to_representation(self, instance):
        return super().to_representation(instance)
