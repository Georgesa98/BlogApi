from rest_framework import serializers

from .models import Like


class CreateLikeSer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

    def create(self, validated_data):
        like = Like.objects.create(**validated_data)
        like.save()
        return like


class GetLikeSer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

    def to_representation(self, instance):
        return super().to_representation(instance)
