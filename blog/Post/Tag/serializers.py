from rest_framework import serializers

from .models import Tag


class TagsSer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class GetTagSer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]
