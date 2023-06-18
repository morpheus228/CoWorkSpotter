from django.db import models


class TgUser(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name='TG ID')
    username = models.CharField(max_length=255, null=True, verbose_name='TG username')
    first_name = models.CharField(max_length=255, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=255, null=True, verbose_name='Фамилия')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return f'{self.first_name} {self.last_name} (@{self.username} id{self.id}'

    class Meta:
        verbose_name = "TG пользователь"
        verbose_name_plural = "TG пользователи"
        ordering = ['created_at']

