from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
<<<<<<< HEAD
=======

    def ready(self):
        from . import signals
>>>>>>> 38ac1d8 (Bug fixed)
