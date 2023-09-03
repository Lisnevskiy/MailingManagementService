from django.apps import AppConfig


class MailingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mailing"

    def ready(self):
        """
        Метод, вызываемый при запуске приложения.
        В этом методе мы импортируем модуль `scheduler`, чтобы обеспечить
        корректную инициализацию запланированных задач при запуске приложения.
        """
        import mailing.scheduler
