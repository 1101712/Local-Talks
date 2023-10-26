from django.apps import AppConfig


# Configuration class for the 'talks' application
class TalksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'localtalks.talks'
    verbose_name = "Talks"

    def ready(self):
        import localtalks.talks.models
