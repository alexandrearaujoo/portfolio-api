from rest_framework import serializers

from .models import Project

from users.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "type",
            "slug",
            "description",
            "link_website",
            "link_repository",
            "img",
            "owner",
        ]
        read_only_fields = ["id"]
