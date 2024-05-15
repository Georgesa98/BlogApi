from rest_framework import serializers

from Users.serializers import GetUserSer
from .models import Comment


class CreateCommentSer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        comment = Comment.objects.create(**validated_data)
        comment.save()
        return comment


class UpdateCommentSer(serializers.ModelSerializer):
    fk_post = serializers.PrimaryKeyRelatedField(read_only=True)
    fk_user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance


class GetCommentSer(serializers.ModelSerializer):
    fk_user = GetUserSer()

    class Meta:
        model = Comment
        fields = "__all__"

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result.pop("fk_post")
        if result.get("fk_comment") == None:
            result.pop("fk_comment")
        return result
