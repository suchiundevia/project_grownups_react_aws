from django.apps import AppConfig


class AccountsAppConfig(AppConfig):
    name = 'account_app'

    def ready(self):
        import account_app.signals
