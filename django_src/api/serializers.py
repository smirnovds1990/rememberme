from rest_framework.serializers import ModelSerializer

from django_src.users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "topics",
            "messages_schedule",
        )
