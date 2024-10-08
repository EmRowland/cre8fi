from django.apps import AppConfig


class AccountsApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts_api"

    def ready(self):
        import accounts_api.signals
