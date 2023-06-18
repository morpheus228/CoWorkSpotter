from django.db import models

TYPE_CHOICES = (
    ('CW', 'Коворкинг'),
    ('F', 'Место питания')
)


class Place(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    about = models.CharField(max_length=500, null=True, blank=True, verbose_name='Краткое описание')
    url = models.CharField(max_length=255, null=True, blank=True, verbose_name='Ссылка')
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, verbose_name='Тип')
    attributes = models.JSONField(verbose_name='Аттрибуты')
    timetable = models.JSONField(verbose_name='Часы работы')
    ymaps = models.CharField(max_length=255, null=True, blank=True, verbose_name='Yandex maps')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"
        ordering = ['created_at']
