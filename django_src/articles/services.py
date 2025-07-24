import logging

from articles.exceptions import NoArticlesException
from articles.models import Article
from articles.repository import ArticleRepository


logger = logging.getLogger(__name__)


class ArticleService:
    """Provide business logic methods for Article."""

    def get_random_article_and_refresh_stats(self) -> Article:
        try:
            articles_amount = ArticleRepository().count_articles()
            random_article = ArticleRepository().get_random_article(
                articles_amount=articles_amount
            )
            ArticleRepository().save_stats(article=random_article)
            logger.info(
                "Send and refresh stats of artcile: %s", random_article.title
            )
            return random_article
        except NoArticlesException as e:
            logger.warning("No articles available: %s", e)
            raise
