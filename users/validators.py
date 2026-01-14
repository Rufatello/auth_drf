import re

from rest_framework import serializers


def validation_password(password):
    if not re.search(r"[0-9]", password):
        raise serializers.ValidationError("Пароль должен содержать хотя бы 1 цифру")
    elif len(password) < 7:
        raise serializers.ValidationError(
            "Длина пароля должна быть больше 7-ми символов"
        )

    elif not re.search(r"[a-zA-Z]", password):
        raise serializers.ValidationError(
            "Пароль должен содержать хотя бы одну латинскую букву"
        )

    elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise serializers.ValidationError("Пароль должен содержать хотя бы 1 символ")

    return password


def validation_password_comparison(password, password2):
    if password != password2:
        raise serializers.ValidationError("Пароли не совпадают")
