from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
from django.conf import settings

class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Email')

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='Группы',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='Права пользователя',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user'
    )

    def __str__(self):
        return self.username

class ConfirmationCode(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    code = models.CharField(max_length=6, verbose_name='Код подтверждения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Код подтверждения'
        verbose_name_plural = 'Коды подтверждения'
    def __str__(self):
        return f'Код для {self.user.username}'

class Ad(models.Model):
    CATEGORIES = [
        ('Tanks', 'Танки'),
        ('Healers', 'Хилы'),
        ('DD', 'ДД'),
        ('Merchants', 'Торговцы'),
        ('Guildmasters', 'Гилдмастеры'),
        ('Questgivers', 'Квестгиверы'),
        ('Blacksmiths', 'Кузнецы'),
        ('Leatherworkers', 'Кожевники'),
        ('Potionsmakers', 'Зельевары'),
        ('Spellmasters', 'Мастера заклинаний'),
    ]
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Автор"
    )
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = HTMLField(verbose_name='Содержание')
    category = models.CharField(
        max_length=20,
        choices=CATEGORIES,
        verbose_name='Категория'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']
    def __str__(self):
        return self.title

class Response(models.Model):
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name='response',
        verbose_name='Объявление'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор отклика'
    )
    text = models.TextField(verbose_name='Текст отклика')
    is_accepted = models.BooleanField(default=False, verbose_name='Принят')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        ordering = ['-created_at']

    def __str__(self):
        return f'Отклик от {self.author.username} на "{self.ad.title}"'





