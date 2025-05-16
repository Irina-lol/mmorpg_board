from django.apps import AppConfig

class AdsConfig(AppConfig):
    default_auto_filed = 'django.db.models.BigAutoField'
    name = 'ads'
    def ready(self):
        import ads.signals
        
