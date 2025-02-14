FROM python:3.12-slim-bookworm
WORKDIR /django_src

COPY pyproject.toml uv.lock ./
RUN apt-get update && \
apt-get install -y --no-install-recommends curl ca-certificates
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"
RUN uv sync --frozen

COPY django_src/ .
RUN chmod +x ./django_entrypoint.sh

ENTRYPOINT ["./django_entrypoint.sh"]
