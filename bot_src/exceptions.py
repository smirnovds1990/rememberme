class RequestException(BaseException):
    """Raise when response.status_code via httpx request is 4xx or 5xx."""

    pass
