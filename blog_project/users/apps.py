from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # for signals
    def ready(self):
        import users.signals
