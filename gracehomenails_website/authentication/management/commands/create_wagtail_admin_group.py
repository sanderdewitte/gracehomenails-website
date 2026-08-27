from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from wagtail.models import Collection, GroupCollectionPermission, GroupPagePermission, Page

from ...groups import WAGTAIL_ADMIN_GROUP


PAGE_PERMISSION_CODENAMES = (
    "add_page",
    "change_page",
    "publish_page",
    "lock_page",
    "unlock_page",
)

IMAGE_PERMISSION_CODENAMES = (
    "add_image",
    "change_image",
    "delete_image",
    "choose_image",
)

DOCUMENT_PERMISSION_CODENAMES = (
    "add_document",
    "change_document",
    "delete_document",
    "choose_document",
)


class Command(BaseCommand):

    help = "Create and configure the Wagtail administrators group."

    def handle(self, *args, **options):

        created = False

        wagtail_admin_group, created = Group.objects.get_or_create(name=WAGTAIL_ADMIN_GROUP)

        if created:
            self.stdout.write(f"  {WAGTAIL_ADMIN_GROUP} group created.")
        else:
            self.stdout.write(f"  {WAGTAIL_ADMIN_GROUP} group already exists.")

        permissions_updated = False

        access_admin_permission = Permission.objects.get(content_type__app_label="wagtailadmin", codename="access_admin")

        if not wagtail_admin_group.permissions.filter(pk=access_admin_permission.pk).exists():
            wagtail_admin_group.permissions.add(access_admin_permission)
            permissions_updated = True

        home_page = Page.objects.get(slug="home")

        for codename in PAGE_PERMISSION_CODENAMES:

            permission = Permission.objects.get(content_type__app_label="wagtailcore", codename=codename)

            _, permission_created = GroupPagePermission.objects.get_or_create(group=wagtail_admin_group, page=home_page, permission=permission)

            if permission_created:
                permissions_updated = True

        root_collection = Collection.objects.get(depth=1)

        for codename in IMAGE_PERMISSION_CODENAMES:

            permission = Permission.objects.get(content_type__app_label="wagtailimages", codename=codename)

            _, permission_created = GroupCollectionPermission.objects.get_or_create(group=wagtail_admin_group, collection=root_collection, permission=permission)

            if permission_created:
                permissions_updated = True

        for codename in DOCUMENT_PERMISSION_CODENAMES:

            permission = Permission.objects.get(content_type__app_label="wagtaildocs", codename=codename)

            _, permission_created = GroupCollectionPermission.objects.get_or_create(group=wagtail_admin_group, collection=root_collection, permission=permission)

            if permission_created:
                permissions_updated = True

        if permissions_updated:
            self.stdout.write(f"  {WAGTAIL_ADMIN_GROUP} group permissions updated.")
