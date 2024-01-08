from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Target


@receiver(post_save, sender=Target)
def create_notification(sender, instance, created, **kwargs):
    if created:
        instance.link = f'https://form.fintechhub.uz/?target_id={instance.id}'
        instance.save()
