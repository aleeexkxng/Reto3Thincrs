from django.apps import AppConfig

class DebitCardAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'debit_card_app'  # This should match the app name in INSTALLED_APPS

default_app_config = 'debit_card_app.DebitCardAppConfig'
