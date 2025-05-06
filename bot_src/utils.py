import httpx

from constants import RANDOM_ARTICLE_URL
from exceptions import RequestException


async def get_random_article():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(RANDOM_ARTICLE_URL)
            response.raise_for_status()
            data = response.json()
            title = data["title"]
            content = data["content"]
            content = content.replace("\r\n", "\n")
            return f"<b>{title}</b>\n\n{content}"
        except httpx.RequestError as exc:
            raise RequestException(
                f"An error occurred while requesting {exc.request.url!r}."
            )
        except httpx.HTTPStatusError as exc:
            raise RequestException(
                f"Error response {exc.response.status_code} "
                f"while requesting {exc.request.url!r}."
            )
            # exc info must be logged
