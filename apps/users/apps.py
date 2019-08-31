from django.apps import AppConfig
from django.db.models.signals import post_save


class UsersConfig(AppConfig):
    label = 'users'
    name = 'users'
    verbose_name = 'Users'

    def ready(self):
        from .signals import signal_user_post_save

        post_save.connect(signal_user_post_save, sender='users.User')
