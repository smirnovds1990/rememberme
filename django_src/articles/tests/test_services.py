import pytest

from articles.exceptions import NoArticlesException
from articles.models import Article, ArticlesStats
from articles.services import ArticleService


def test_the_exception_is_raised_without_articles_in_db(db) -> None:
    with pytest.raises(NoArticlesException):
        ArticleService().get_random_article_and_refresh_stats()


def test_get_random_article_and_refresh_stats_gives_an_article(
    two_test_articles: tuple[Article, Article],
) -> None:
    random_article = ArticleService().get_random_article_and_refresh_stats()
    assert random_article in two_test_articles


def test_showing_counter_is_increased_after_getting_article(
    one_test_article: Article,
) -> None:
    ArticleService().get_random_article_and_refresh_stats()
    article_stats = ArticlesStats.objects.get(article=one_test_article)
    assert article_stats.showing_counter == 1
