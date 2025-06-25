from articles.models import Article
from articles.repository import ArticleRepository


class ArticleService:
    """Provide business logic methods for Article."""

    def get_random_article_and_refresh_stats(self) -> Article:
        articles_amount = ArticleRepository().count_articles()
        random_article = ArticleRepository().get_random_article(
            articles_amount=articles_amount
        )
        ArticleRepository().save_stats(article=random_article)
        return random_article
