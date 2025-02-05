
FROM python:3.11-slim AS base

RUN pip install --no-cache-dir uv uvicorn

WORKDIR /app

COPY . .

RUN uv venv

RUN . .venv/bin/activate && uv sync

ENV ENVIRONMENT=prod

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
