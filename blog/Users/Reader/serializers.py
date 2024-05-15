from rest_framework import serializers

from Users.serializers import CreateUserSer, UpdateUserSer

from .models import Reader


class CreateReaderSer(serializers.ModelSerializer):
    user = CreateUserSer()

    class Meta:
        model = Reader
        fields = "__all__"

    def create(self, validated_data):
        userData = validated_data.pop("user")
        userData["role"] = "Reader"
        user_ser = CreateUserSer(data=userData)
        if user_ser.is_valid():
            user = user_ser.save()
            reader = Reader.objects.create(user=user, **validated_data)
            return reader
        else:
            pass


class UpdateReaderSer(serializers.ModelSerializer):
    user = UpdateUserSer()

    class Meta:
        model = Reader
        fields = "__all__"

    def update(self, instance, validated_data):
        userData = validated_data.pop("user")
        user_ser = UpdateUserSer(data=userData, instance=instance.user)
        if user_ser.is_valid():
            user_ser.save()
            instance.save()
        return instance


class GetReaderSer(serializers.ModelSerializer):
    class Meta:
        model = Reader
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
