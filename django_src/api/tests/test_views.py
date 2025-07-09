from django.urls import reverse
from rest_framework import status


def test_view_with_monkeypatch(api_client, monkeypatch):
    fake_data = {"title": "Foo", "content": "Bar"}

    monkeypatch.setattr(
        "api.views.ArticleService.get_random_article_and_refresh_stats",
        lambda self: None,
    )
    monkeypatch.setattr("api.views.ArticleSerializer.data", fake_data)

    url = reverse("random-article")
    resp = api_client.get(url)

    assert resp.status_code == status.HTTP_200_OK
    assert resp.json() == fake_data
