from django.urls import path

from django_src.api.views import ScheduleCreateView, ScheduleUpdateDestroyView


urlpatterns = [
    path("schedule/", ScheduleCreateView.as_view(), name="schedule-create"),
    path(
        "schedule/<str:username>/",
        ScheduleUpdateDestroyView.as_view(),
        name="schedule-update-destroy",
    ),
]
