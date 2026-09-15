from rest_framework import serializers
from .models import User,Task

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "role"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
            role=validated_data.get("role", "staff")
        )
        return user
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"