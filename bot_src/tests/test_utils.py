from http import HTTPStatus
from unittest.mock import MagicMock, patch

import pytest
from httpx import HTTPStatusError, RequestError
from utils import form_message, get_random_article

from exceptions import RequestException


def test_form_message(article_data: dict[str, str]) -> None:
    assert (
        form_message(article_data)
        == f"<b>{article_data["title"]}</b>\n\n{article_data["content"]}"
    )


@patch("utils.httpx.AsyncClient.get")
@pytest.mark.asyncio
async def test_successful_get_random_article(
    mock_get, article_data: dict[str, str]
) -> None:
    mock_response = MagicMock()
    mock_response.json.return_value = article_data
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response
    assert await get_random_article() == "<b>Test Title</b>\n\nTest content."


@patch("utils.httpx.AsyncClient.get")
@pytest.mark.asyncio
async def test_get_random_article_handles_request_error(mock_get) -> None:
    mock_get.side_effect = RequestError(
        "Network error",
        request=MagicMock(url="http://test.url"),
    )
    with pytest.raises(RequestException) as error:
        await get_random_article()
    assert "An error occurred while requesting" in str(error.value)


@patch("utils.httpx.AsyncClient.get")
@pytest.mark.asyncio
async def test_get_random_article_handles_http_status_error(mock_get) -> None:
    mock_get.side_effect = HTTPStatusError(
        "An error occured",
        request=MagicMock(url="http://test.url"),
        response=MagicMock(status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value),
    )
    with pytest.raises(RequestException) as error:
        await get_random_article()
    assert "Error response" in str(error.value)
    assert "while requesting" in str(error.value)
