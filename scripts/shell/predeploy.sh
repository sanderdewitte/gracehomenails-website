#!/bin/sh

set -eu

DATABASE_WAIT_TIMEOUT=60
DATABASE_WAIT_INTERVAL=5
DATABASE_WAIT_ELAPSED=0

DATABASE_CONNECTION_CHECK='from django.db import connection; connection.ensure_connection()'

echo "Waiting for database connection..."

while ! uv run python manage.py shell -c "$DATABASE_CONNECTION_CHECK" >/dev/null 2>&1; do
  if [ "$DATABASE_WAIT_ELAPSED" -ge "$DATABASE_WAIT_TIMEOUT" ]; then
    echo "Database connection did not become available within ${DATABASE_WAIT_TIMEOUT} seconds." >&2
    exit 1
  fi
  sleep "$DATABASE_WAIT_INTERVAL"
  DATABASE_WAIT_ELAPSED=$((DATABASE_WAIT_ELAPSED + DATABASE_WAIT_INTERVAL))
done

echo "Database connection available."

uv run python manage.py migrate --noinput
uv run python manage.py create_wagtail_admin_group
uv run python manage.py create_initial_services_page

exit 0
