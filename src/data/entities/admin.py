import peewee
from .base import BaseEntity


class Admin(BaseEntity):
    """Администратор бота (им присылаются отчеты)"""

    # Идентификатор пользователя в телеграме
    telegram_id = peewee.CharField(primary_key=True)

    # Признак активности админа
    is_active = peewee.BooleanField()
