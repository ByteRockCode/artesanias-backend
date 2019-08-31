from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

from categories.models import Category
from stores.models import Store


def add_permissions_to_user(user):
    def get_verbose_names(models):
        return [m._meta.verbose_name for m in models]

    models = (
        Store,
    )

    models_only_view = (
        Category,
    )

    permissions = Permission.objects.filter(
        Q(
            content_type__model__in=get_verbose_names(models),
        ) |
        Q(
            content_type__model__in=get_verbose_names(models_only_view),
            codename__istartswith='view_',
        )
    )

    for permission in permissions:
        user.user_permissions.add(permission)
