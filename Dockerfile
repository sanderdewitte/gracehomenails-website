# Copy uv from its official image.
FROM ghcr.io/astral-sh/uv:0.12.3 AS uv

FROM python:3.13-slim-bookworm

# Runtime libraries required by Wagtail/Pillow.
RUN apt-get update --yes --quiet \
    && apt-get install --yes --quiet --no-install-recommends \
        libjpeg62-turbo \
        libwebp7 \
    && rm -rf /var/lib/apt/lists/*

# Install uv.
COPY --from=uv /uv /uvx /bin/

# Create the non-root application user.
RUN useradd --create-home wagtail

WORKDIR /app
RUN chown wagtail:wagtail /app

# Install locked dependencies separately from the application source
# to maximize Docker layer caching.
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

# Copy the application source.
COPY --chown=wagtail:wagtail . .

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PORT=8000

USER wagtail

# Collect static files into the image.
RUN DJANGO_SETTINGS_MODULE=gracehomenails_website.settings.build \
    python manage.py collectstatic --noinput --clear

EXPOSE 8000

CMD ["gunicorn", "gracehomenails_website.wsgi:application", "--bind", "0.0.0.0:8000"]
