from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
)

from api.serializers import UserSerializer
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
        return self.create(request, *args, **kwargs)


class ScheduleUpdateDestroyView(
    DestroyModelMixin, UpdateModelMixin, GenericAPIView
):
    """Update or delete a user messaging schedule."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
