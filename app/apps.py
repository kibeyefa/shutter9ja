from django.apps import AppConfig


class EntriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'  # or whatever your app is called

    def ready(self):
        import app.signals  # make sure to import signals here