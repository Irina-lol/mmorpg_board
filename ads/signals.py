from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Response

@receiver(post_save, sender=Response)
def notify_about_response(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Новый отклик!',
            f'Пользователь {instance.author} оставил отклик: {instance.text}',
            'from@example.com',
            [instance.ad.author.email],
            fail_silently=False,
        )