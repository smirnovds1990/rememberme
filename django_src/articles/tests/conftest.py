import pytest

from articles.models import Article, Topic
from articles.repository import ArticleRepository


@pytest.fixture
def testing_topic(db) -> Topic:
    return Topic.objects.create(name="Test topic")


@pytest.fixture
def articles_repository() -> ArticleRepository:
    return ArticleRepository()


@pytest.fixture
def one_test_article(db, testing_topic: Topic) -> Article:
    return Article.objects.create(
        title="Test", content="...", is_deleted=False, topic=testing_topic
    )


@pytest.fixture
def two_test_articles(db, testing_topic: Topic) -> tuple[Article, Article]:
    first_article = Article.objects.create(
        title="Article 1", content="Text", topic=testing_topic
    )
    second_article = Article.objects.create(
        title="Article 2", content="Text", topic=testing_topic
    )
    return first_article, second_article


@pytest.fixture
def deleted_and_non_deleted_articles(
    db, testing_topic: Topic
) -> tuple[Article, Article]:
    deleted_article = Article.objects.create(
        title="Deleted",
        content="...",
        is_deleted=True,
        topic=testing_topic,
    )
    non_deleted_article = Article.objects.create(
        title="Active",
        content="...",
        is_deleted=False,
        topic=testing_topic,
    )
    return deleted_article, non_deleted_article
