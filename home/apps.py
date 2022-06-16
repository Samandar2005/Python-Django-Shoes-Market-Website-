from django.apps import AppConfig
from django.contrib import admin
from .models import Profile
admin.site.register(Profile)


class HomeConfig(AppConfig):
    name = 'home'


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # add this
    def ready(self):
        import users.signals  # noqa
