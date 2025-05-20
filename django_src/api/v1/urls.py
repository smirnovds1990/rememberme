from django.urls import path

from api.views import (
    RandomArticleRetrieveView,
    ScheduleCreateView,
    ScheduleUpdateDestroyView,
)



urlpatterns = [
    path("schedule/", ScheduleCreateView.as_view(), name="schedule-create"),
    path(
        "schedule/<str:username>/",
        ScheduleUpdateDestroyView.as_view(),
        name="schedule-update-destroy",
    ),
    path(
        "random-article/",
        RandomArticleRetrieveView.as_view(),
        name="random-article",
    ),
]
