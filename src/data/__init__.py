from typing import List

from .entities import db_proxy, User, Admin


def set_admins(admin_ids: List[str]):
    for admin_id in admin_ids:
        if Admin.get_or_none(Admin.telegram_id == admin_id) is None:
            Admin.create(
                telegram_id=admin_id,
                is_active=True
            )


def initialize_db(connection, admin_ids: List[str]):
    db_proxy.initialize(connection)

    with db_proxy:
        db_proxy.create_tables([User, Admin])

    set_admins(admin_ids)
