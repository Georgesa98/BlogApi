from rest_framework import serializers

from Post.models import Post
from Post.Like.models import Like, LikeType
from Post.Tag.serializers import GetTagSer, TagsSer
from Post.Tag.models import Tag
from Post.Comment.models import Comment
from Post.Comment.serializer import GetCommentSer


class CreatePostSer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = Post
        fields = [
            "fk_author_id",
            "created_at",
            "title",
            "image",
            "content",
            "tags",
        ]

    def create(self, validated_data):
        tags = validated_data.pop("tags")
        post = Post.objects.create(**validated_data)
        post.save()
        post.tags.set(tags)
        return post


class UpdatePostSer(serializers.ModelSerializer):
    fk_author_id = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)
    content = serializers.CharField(required=False)
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = Post
        fields = [
            "fk_author_id",
            "title",
            "image",
            "content",
            "tags",
        ]

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.image = validated_data.get("image", instance.image)
        instance.content = validated_data.get("content", instance.content)
        tags = validated_data.get("tags")
        if tags:
            instance.tags.set(tags)
        instance.save()
        return instance


class GetPostSer(serializers.ModelSerializer):
    title = serializers.CharField()
    image = serializers.ImageField()
    content = serializers.CharField()
    tags = GetTagSer(many=True)
    comments = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        likes = Like.objects.filter(post=obj)
        likeList = []
        for like in likes:
            like_dict = {
                "type": like.type.type,
                "count": Like.objects.filter(post=obj).count(),
            }
            likeList.append(like_dict)
        return likeList

    def get_comments(self, obj):
        comments = Comment.objects.filter(fk_post=obj)
        serializer = GetCommentSer(comments, many=True)
        return serializer.data

    class Meta:
        model = Post
        fields = [
            "id",
            "fk_author_id",
            "created_at",
            "title",
            "image",
            "content",
            "tags",
            "comments",
            "likes_count",
        ]

    def to_representation(self, instance):
        return super().to_representation(instance)
