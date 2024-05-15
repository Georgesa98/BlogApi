from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from Users.models import Users
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from Users.Author.models import Author
from Users.Reader.models import Reader


class CreateUserSer(serializers.ModelSerializer):
    pfp = serializers.ImageField(required=False)
    password = serializers.CharField(write_only=True)
    role = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Users
        fields = [
            "id",
            "first_name",
            "last_name",
            "gender",
            "role",
            "pfp",
            "username",
            "password",
        ]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        instance = Users.objects.create(**validated_data)
        return instance


class UpdateUserSer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    pfp = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)

    class Meta:
        model = Users
        fields = ["first_name", "last_name", "pfp", "username", "gender"]

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.pfp = validated_data.get("pfp", instance.pfp)
        instance.role = validated_data.get("role", instance.role)
        instance.username = validated_data.get("username", instance.username)
        instance.gender = validated_data.get("gender", instance.gender)
        instance.save()
        return instance


class GetUserSer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            "first_name",
            "last_name",
            "pfp",
            "username",
            "gender",
            "role",
        ]

    def to_representation(self, instance):
        return super().to_representation(instance)


class TokenObtainSer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        if user.role == "Author":
            author = Author.objects.get(user=user)
            token["author_id"] = author.id
        elif user.role == "Reader":
            reader = Reader.objects.get(user=user)
            token["reader_id"] = reader.id
        return token
