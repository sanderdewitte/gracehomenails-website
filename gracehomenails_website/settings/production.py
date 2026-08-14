import os

import dj_database_url

from .base import *

DEBUG = False

# Configure the production PostgreSQL database from the environment.
DATABASES = {
    "default": dj_database_url.config(
        env="DATABASE_URL",
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Load production secrets and host configuration from the environment.
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ["DJANGO_ALLOWED_HOSTS"].split(",")
    if host.strip()
]

# Trust HTTPS information forwarded by the Kubernetes ingress.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Enable HSTS conservatively without applying it to subdomains or preload lists.
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

# Only send authentication-related cookies over HTTPS.
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Set the public base URL used by Wagtail for absolute URLs.
WAGTAILADMIN_BASE_URL = os.environ["WAGTAILADMIN_BASE_URL"]

# Use hashed and compressed static files in production.
# See https://whitenoise.readthedocs.io/en/latest/
STORAGES["staticfiles"]["BACKEND"] = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Configure OpenID Connect authentication from the environment.
OIDC_GROUPS_ATTRIBUTE = os.environ["OIDC_GROUPS_ATTRIBUTE"]
OIDC_PROVIDER_ID = os.environ["OIDC_PROVIDER_ID"]
OIDC_CLIENT_NAME = os.environ["OIDC_CLIENT_NAME"]
SOCIALACCOUNT_PROVIDERS = {
    "openid_connect": {
        "SCOPE": [
            scope.strip()
            for scope in os.environ["OIDC_SCOPE"].split()
            if scope.strip()
        ],
        "APPS": [
            {
                "provider_id": OIDC_PROVIDER_ID,
                "name": OIDC_CLIENT_NAME,
                "client_id": os.environ["OIDC_CLIENT_ID"],
                "secret": os.environ["OIDC_CLIENT_SECRET"],
                "settings": {
                    "server_url": os.environ["OIDC_ISSUER"],
                },
            },
        ],
    }
}

# Redirect logout through the configured OpenID Connect provider.
ACCOUNT_LOGOUT_REDIRECT_URL = os.environ["OIDC_LOGOUT_REDIRECT_URL"]

try:
    from .local import *
except ImportError:
    pass
