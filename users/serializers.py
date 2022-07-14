from rest_framework import serializers

from .models import User

from techs.serializers import TechSerializer

class UserSerializer(serializers.ModelSerializer):
    techs = TechSerializer(many=True)
    class Meta:
        models = User
        fields = "__all__"
        read_only_fields = ['id']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)