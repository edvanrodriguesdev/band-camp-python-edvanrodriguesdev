from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
            if key == "password":
                instance.set_password(value)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "full_name",
            "artistic_name",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {"validators": [
                UniqueValidator(queryset=User.objects.all(), message="A user with that username already exists.")
            ]},
            "email": {"validators": [
                UniqueValidator(queryset=User.objects.all(), message="This field must be unique.")
            ]},
                        }

