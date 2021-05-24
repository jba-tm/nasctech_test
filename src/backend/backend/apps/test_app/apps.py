from django.apps import AppConfig


class TestAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.apps.test_app'
    label = 'test_app'
