import peewee
from .base import BaseEntity
from datetime import datetime


class User(BaseEntity):
    """Модель пользователя."""

    # Идентификатор пользователя в телеграме
    telegram_id = peewee.CharField(primary_key=True)

    # Имя
    first_name = peewee.CharField()

    # Фамилия
    last_name = peewee.CharField(null=True)

    # Имя и Фамилия
    full_name = peewee.CharField()

    # Обращение (@никнейм)
    mention = peewee.CharField()

    # Никнейм
    username = peewee.CharField()

    # Ссылка на пользователя
    url = peewee.CharField()

    # Признак бота
    is_bot = peewee.BooleanField()

    # Дата добавления
    creation_date = peewee.DateTimeField(default=datetime.now)

    # Номер представительства
    representative_office_number = peewee.IntegerField(null=True)
