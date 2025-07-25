import logging

import httpx

from constants import RANDOM_ARTICLE_URL
from exceptions import RequestException


logger = logging.getLogger(__name__)


def form_message(data: dict[str, str]) -> tuple[str, str]:
    title = data["title"]
    content = data["content"]
    content = content.replace("\r\n", "\n")
    return title, f"<b>{title}</b>\n\n{content}"


async def get_random_article():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(RANDOM_ARTICLE_URL)
            response.raise_for_status()
            data = response.json()
            return form_message(data)
        except httpx.RequestError as exc:
            logger.warning("Got RequestError: %s", exc)
            raise RequestException(
                f"An error occurred while requesting {exc.request.url!r}."
            )
        except httpx.HTTPStatusError as exc:
            logger.warning("Got HTTPStatusError: %s", exc)
            raise RequestException(
                f"Error response {exc.response.status_code} "
                f"while requesting {exc.request.url!r}."
            )
