from rest_framework.serializers import ModelSerializer

from articles.models import Article
from users.models import User


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


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "content")
