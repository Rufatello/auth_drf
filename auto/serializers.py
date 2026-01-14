from rest_framework import serializers

from auto.models import AutoPhoto, Auto


class AutoPhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = AutoPhoto
        fields = ("photo",)


class AutoCreateSerializers(serializers.ModelSerializer):
    photos = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )

    class Meta:
        model = Auto
        fields = ("model", "make", "photos", "years", "car_body")

    def create(self, validated_data):
        photos = validated_data.pop("photos", [])
        auto = Auto.objects.create(**validated_data)

        for photo in photos:
            AutoPhoto.objects.create(auto=auto, photo=photo)

        return auto


class AutoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = (
            "model",
            "make",
            "years",
            "car_body",
        )


class AutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = ("id", "model", "make", "photos", "years", "car_body", "user")
