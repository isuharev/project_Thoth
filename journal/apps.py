from django.apps import AppConfig


class JournalConfig(AppConfig):
    name = 'journal'     # Здесь указываем исходное имя приложения
    verbose_name = "Журнал регистрации документов"   # А здесь, имя которое необходимо отобразить в админке
