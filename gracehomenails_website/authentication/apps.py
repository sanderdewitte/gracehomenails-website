from django.apps import AppConfig


class AuthenticationConfig(AppConfig):

    name = "gracehomenails_website.authentication"

    def ready(self):

        from . import signals  # noqa: F401
