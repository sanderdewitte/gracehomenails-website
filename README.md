# Grace Home Nails Website

Wagtail CMS website for Grace Home Nails.

## Technology stack

-   Python 3.13
-   Django 6
-   Wagtail 7.4
-   PostgreSQL
-   django-allauth for OpenID Connect authentication
-   WhiteNoise for static files
-   Gunicorn WSGI HTTP server
-   uv for Python dependency and environment management

## Local development

Create or update the local environment from the lock file:

``` bash
uv sync
```

Apply database migrations:

``` bash
uv run python manage.py migrate
```

Start the Django development server:

``` bash
uv run python manage.py runserver
```

The development configuration uses `gracehomenails_website.settings.dev` and a local SQLite database by default.

Run the Django system checks with:

``` bash
uv run python manage.py check
```

## Production and containers

The application is packaged as a container image using the repository `Dockerfile`.

Build the image locally with:

``` bash
docker build -t gracehomenails-website:test .
```

The container uses the production Django settings module:

``` text
gracehomenails_website.settings.production
```

Production uses PostgreSQL and serves collected static assets with `WhiteNoise`.

Runtime configuration and secrets are supplied through environment variables;
secrets are not stored in the repository.

## Environment variables

The production configuration uses the following environment variables:

| Variable | Purpose |
| --- | --- |
| `DATABASE_URL` | PostgreSQL connection URL |
| `DJANGO_SECRET_KEY` | Django secret key |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated allowed host names |
| `WAGTAILADMIN_BASE_URL` | Public base URL for the Wagtail admin |
| `OIDC_PROVIDER_ID` | `django-allauth` OpenID Connect provider identifier |
| `OIDC_ISSUER` | OpenID Connect issuer URL |
| `OIDC_CLIENT_NAME` | Display name of the SSO provider |
| `OIDC_SCOPE` | Space-separated OpenID Connect scopes |
| `OIDC_GROUPS_ATTRIBUTE` | Claim containing OIDC group memberships |
| `OIDC_LOGOUT_REDIRECT_URL` | Redirect destination after logout |
| `OIDC_CLIENT_ID` | OpenID Connect client ID |
| `OIDC_CLIENT_SECRET` | OpenID Connect client secret |

Real credentials and secrets must never be committed.
If an environment-file template is added, use `.env.sample` or `.env.example`;
both are permitted by the repository `.gitignore`.

## Authentication

Production authentication uses OpenID Connect through `django-allauth`.

SSO is the normal Wagtail login method; local username/password authentication remains available as a secondary login method.

OIDC group claims can synchronize relevant Wagtail group membership.

Local development does not require an OIDC provider.

## License

Copyright (c) 2026 Grace Home Nails. All rights reserved.

The source code is publicly viewable but is not open-source software.
See the [LICENSE](LICENSE) file for the applicable terms.
