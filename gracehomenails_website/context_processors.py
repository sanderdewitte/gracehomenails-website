from django.conf import settings


def oidc(request):

    return {
        "oidc_provider_id": getattr(settings, "OIDC_PROVIDER_ID", None),
        "oidc_client_name": getattr(settings, "OIDC_CLIENT_NAME", None),
    }
