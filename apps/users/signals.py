from .tasks import add_permissions_to_user


def signal_user_post_save(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        add_permissions_to_user(instance)

    if not instance.is_staff:
        instance.is_staff = True
        instance.save()
