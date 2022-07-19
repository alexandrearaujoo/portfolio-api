from rest_framework import serializers

from .models import User
from techs.models import Tech

from techs.serializers import TechSerializer


class UserSerializer(serializers.ModelSerializer):
    techs = TechSerializer(many=True)

    class Meta:
        model = User
        fields = ["id", "name", "email", "password", "techs"]
        read_only_fields = ["id"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        techs = validated_data.pop("techs")

        user = User.objects.create_user(**validated_data)

        for tech in techs:
            t, _ = Tech.objects.get_or_create(**tech)
            user.techs.add(t)

        return user

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "techs" and type(value) == list:
                for tech in value:
                    t, _ = Tech.objects.get_or_create(**tech)
                    instance.techs.add(t)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)


class ListUserProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email"]
        read_only_fields = ["id"]
