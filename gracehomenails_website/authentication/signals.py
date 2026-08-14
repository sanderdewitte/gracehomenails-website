from allauth.account.signals import user_signed_up
from allauth.socialaccount.signals import social_account_updated
from django.dispatch import receiver

from .groups import sync_wagtail_admin_group


@receiver(user_signed_up)
def sync_wagtail_admin_group_on_signup(sender, request, user, **kwargs):

    sociallogin = kwargs.get("sociallogin")

    if sociallogin is not None:
        sync_wagtail_admin_group(user, sociallogin)


@receiver(social_account_updated)
def sync_wagtail_admin_group_on_login(sender, request, sociallogin, **kwargs):

    sync_wagtail_admin_group(sociallogin.user, sociallogin)
