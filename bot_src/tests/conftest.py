import pytest


@pytest.fixture
def article_data() -> dict[str, str]:
    return {
        "title": "Test Title",
        "content": "Test content.",
    }
