from django.conf import settings
from django.contrib.auth.models import Group


WAGTAIL_ADMIN_GROUP = "Wagtail Admins"


def sync_wagtail_admin_group(user, sociallogin):

    groups_attribute = settings.OIDC_GROUPS_ATTRIBUTE

    userinfo = sociallogin.account.extra_data.get("userinfo", {})
    id_token = sociallogin.account.extra_data.get("id_token", {})

    user_oidc_groups = (
        userinfo.get(groups_attribute)
        or id_token.get(groups_attribute)
        or []
    )

    if isinstance(user_oidc_groups, str):
        user_oidc_groups = [user_oidc_groups]

    is_wagtail_admin = WAGTAIL_ADMIN_GROUP in user_oidc_groups
    wagtail_admin_group, _ = Group.objects.get_or_create(name=WAGTAIL_ADMIN_GROUP)

    if is_wagtail_admin:
        user.groups.add(wagtail_admin_group)
    else:
        user.groups.remove(wagtail_admin_group)

    if user.is_staff != is_wagtail_admin:
        user.is_staff = is_wagtail_admin
        user.save(update_fields=["is_staff"])
