from rest_framework import serializers

from Users.Author.models import Author
from Users.serializers import CreateUserSer, UpdateUserSer
from Users.models import Users


class CreateAuthorSer(serializers.ModelSerializer):
    user = CreateUserSer()

    class Meta:
        model = Author
        fields = ["user"]

    def create(self, validated_data):
        userData = validated_data.pop("user")
        userData["role"] = "Author"
        user_ser = CreateUserSer(data=userData)
        if user_ser.is_valid():
            user = user_ser.save()
            author = Author.objects.create(user=user, **validated_data)
            return author
        else:
            pass


class UpdateAuthorSer(serializers.ModelSerializer):
    user = UpdateUserSer()

    class Meta:
        model = Author
        fields = "__all__"

    def update(self, instance, validated_data):
        userData = validated_data.pop("user")
        user_ser = UpdateUserSer(data=userData, instance=instance.user)
        if user_ser.is_valid():
            user_ser.save()
            instance.save()
        return instance


class GetAuthorSer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

    def to_representation(self, instance):
        representation = {}
        representation["id"] = instance.id
        representation["first_name"] = instance.user.first_name or None
        representation["last_name"] = instance.user.last_name or None
        representation["gender"] = instance.user.gender or None
        representation["username"] = instance.user.username or None
        representation["pfp"] = instance.user.pfp or None
        return representation
