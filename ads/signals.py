from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Response

@receiver(post_save, sender=Response)
def notify_about_response(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject=f'Новый отклик на "{instance.ad.title}"',
            message=f'Пользователь {instance.author.username} оставил отклик:\n\n{instance.text}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.ad.author.email],
            fail_silently=False,
        )
    elif instance.is_accepted:
        send_mail(
            subject=f'Ваш отклик принят!',
            message=f'Автор {instance.ad.author.username} принял ваш отклик на объявление "{instance.ad.title}"',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.author.email],
            fail_silently=False,
        )