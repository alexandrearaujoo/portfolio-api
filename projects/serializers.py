from rest_framework import serializers
from rest_framework.validators import UniqueValidator


from .models import Project

from users.models import User
from users.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ["id"]
        extra_kwargs = {
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(), message="Email already exists"
                    )
                ]
            },
            "password": {"write_only": True},
        }
