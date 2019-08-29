from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


def add_permissions_to_user(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        if not instance.user_permissions.exists():
            from stores.models import Store

            models = (
                Store,
            )

            content_types = ContentType.objects.filter(
                model__in=[m._meta.verbose_name for m in models],
            )

            permissions = Permission.objects.filter(content_type__in=content_types)

            for permission in permissions:
                instance.user_permissions.add(permission)

        if not instance.is_staff:
            instance.is_staff = True
            instance.save()
