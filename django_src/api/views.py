
import random

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
)

from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ArticleSerializer, UserSerializer
from articles.exceptions import NoArticlesException
from articles.models import Article

from users.models import User


class ScheduleCreateView(
    CreateModelMixin,
    GenericAPIView,
):
    """Create a user messaging schedule.

    Get a username, wanted topics, schedule hours from the bot
    and create a user instance.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class ScheduleUpdateDestroyView(
    DestroyModelMixin, UpdateModelMixin, GenericAPIView
):
    """Update or delete a user messaging schedule."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class RandomArticleRetrieveView(APIView):
    """Get a random article to send it via bot."""

    def get(self, request):
        articles_amount = Article.objects.count()
        if articles_amount == 0:
            raise NoArticlesException("Sorry. There are no articles yet.")
        random_index = random.randint(0, articles_amount - 1)
        random_article = Article.objects.all()[random_index]
        serializer = ArticleSerializer(random_article)
        return Response(serializer.data)
