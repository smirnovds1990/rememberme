import random

from articles.exceptions import NoArticlesException
from articles.models import Article, ArticlesStats


class ArticleRepository:
    """Provide methods to interact with DB for Article model."""

    def count_articles(self) -> int:
        """Check if there are any articles in DB."""
        articles_amount = Article.objects.filter(is_deleted=False).count()
        if articles_amount == 0:
            raise NoArticlesException("Sorry. There are no articles yet.")
        return articles_amount

    def get_random_article(self, articles_amount: int) -> Article:
        """Get a random article with a number of artciles in DB."""
        random_index = random.randint(0, articles_amount - 1)
        return Article.objects.filter(is_deleted=False)[random_index]

    def save_stats(self, article: Article) -> None:
        """Increment stats counter for every shown article."""
        stats, _ = ArticlesStats.objects.get_or_create(article=article)
        stats.showing_counter += 1
        stats.save()
