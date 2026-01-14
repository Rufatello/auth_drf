from rest_framework import serializers
from users.models import User
from users.validators import validation_password, validation_password_comparison


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "surname")


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validation_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "surname",
            "password",
            "password2",
        )

    def validate(self, data):
        validation_password_comparison(data["password"], data["password2"])
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.pop("password2")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name", "last_name", "surname"
        )