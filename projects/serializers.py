from rest_framework import serializers

from .models import Project

from users.serializers import ListUserProjectsSerializer


class ProjectSerializer(serializers.ModelSerializer):
    owner = ListUserProjectsSerializer(read_only=True)

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
