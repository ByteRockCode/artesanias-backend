from django.apps import AppConfig
from django.db.models.signals import post_save


class UsersConfig(AppConfig):
    label = 'users'
    name = 'users'
    verbose_name = 'Users'

    def ready(self):
        from .signals import add_permissions_to_user

        post_save.connect(add_permissions_to_user, sender='users.User')
