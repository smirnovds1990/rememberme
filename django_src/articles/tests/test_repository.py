import pytest

from articles.exceptions import NoArticlesException
from articles.models import Article, ArticlesStats, Topic
from articles.repository import ArticleRepository


pytestmark = pytest.mark.django_db


def test_count_articles_returns_correct_count(
    testing_topic: Topic,
    two_test_articles: tuple[Article, Article],
    articles_repository: ArticleRepository,
) -> None:
    assert articles_repository.count_articles() == 2


def test_count_articles_raise_correct_exception_if_no_articles_exist(
    articles_repository: ArticleRepository,
) -> None:
    with pytest.raises(NoArticlesException):
        articles_repository.count_articles()


def test_get_random_article_returns_only_non_deleted(
    monkeypatch,
    deleted_and_non_deleted_articles: tuple[Article, Article],
    articles_repository: ArticleRepository,
) -> None:
    # Control the choice of random.randint()
    monkeypatch.setattr("articles.repository.random.randint", lambda a, b: 0)

    article = articles_repository.get_random_article(
        articles_amount=articles_repository.count_articles()
    )
    assert article == deleted_and_non_deleted_articles[1]
    assert not article.is_deleted


def test_save_stats_creates_new_stats(
    one_test_article: Article, articles_repository: ArticleRepository
) -> None:
    articles_repository.save_stats(one_test_article)
    stats = ArticlesStats.objects.get(article=one_test_article)
    assert stats.showing_counter == 1


def test_save_stats_increments_existing_counter(
    one_test_article: Article, articles_repository: ArticleRepository
) -> None:
    stats = ArticlesStats.objects.create(
        article=one_test_article, showing_counter=5
    )
    articles_repository.save_stats(one_test_article)
    stats.refresh_from_db()
    assert stats.showing_counter == 6
