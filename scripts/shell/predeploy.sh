#!/bin/sh

set -eu

uv run python manage.py migrate --noinput
uv run python manage.py create_initial_services_page

exit 0
