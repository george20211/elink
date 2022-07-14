from secrets import choice
from django.db import models
from users.models import User
from django.core.validators import URLValidator


class LinkRegUser(models.Model):
    # Автор
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='owner_link', null=False)
    # Изначальная ссылка
    linked = models.TextField(validators=[URLValidator()], max_length=5000, null=False) #models.URLField(max_length=5000, null=False)
    # сгенерированная ссылка
    linked_link = models.CharField(db_index=True, max_length=20)
    # дата добавления
    date_add = models.DateTimeField(null=True, blank=True)
    # описание
    description = models.CharField(null=True, max_length=1000, blank=True)
    #включить лимит по переходам
    limit = models.BooleanField(null=False, default=0)
    # количество переходов по ссылке
    limited_link = models.PositiveIntegerField(db_index=True, default=0, null=True, blank=True)
    # пароль на ссылку
    secure_link = models.CharField(default=0, max_length=10)
    # с какой даты ссылка активна
    start_link = models.DateTimeField(null=True, blank=True)
    # дата остановки доступа к ссылке
    date_stop = models.DateTimeField(null=True, blank=True)
    # Сколько раз перешли по ссылке всего
    how_many_link = models.IntegerField(db_index=True, default=0)
    #Повторные переходы
    again_how_many_link = models.IntegerField(db_index=True, default=0)
    #Разрешить просмотр статистики всем людям
    public_stat = models.BooleanField(db_index=True, default=False)

    class Meta:
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(fields=['linked_link'], name='unique_generate_link')
            ]

class InfoLink(models.Model):
    # Дата просмотра ссылки
    date_check = models.DateTimeField(db_index=True)
    # Какая ссылка открыта
    link_check = models.ForeignKey(LinkRegUser, on_delete=models.PROTECT, related_name='link_link', null=False)
    # Из какой страны перешли по ссылке
    country_check_id = models.SmallIntegerField(db_index=True)
    #Устройство
    device_id = models.SmallIntegerField(db_index=True)

class NoRegUser(models.Model):
    # Изначальная ссылка
    linked = models.URLField(max_length=5000, null=False)
    # дата добавления
    date_add = models.DateTimeField(null=True, blank=True)
