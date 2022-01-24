from django.apps import AppConfig


class VerifyConfig(AppConfig):
    name = 'verify'

    def ready(self):
        import verify.signals
