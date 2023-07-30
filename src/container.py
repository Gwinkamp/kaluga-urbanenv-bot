import logging.config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dependency_injector import containers, providers
from playhouse.db_url import connect

from data import initialize_db
from handlers import register_handlers


class Container(containers.DeclarativeContainer):
    """Dependency injection container"""

    config = providers.Configuration()

    configure_logging = providers.Resource(logging.config.fileConfig, fname='logging.ini')

    # database
    db_connection = providers.Callable(connect, url=config.db_connection_string)

    init_database = providers.Resource(initialize_db, connection=db_connection, admin_ids=config.admins)

    # bot
    bot = providers.Singleton(Bot, token=config.bot_token)
    storage = providers.Singleton(MemoryStorage)
    dispatcher = providers.Singleton(Dispatcher, bot=bot, storage=storage)

    handlers = providers.Resource(register_handlers, dispatcher=dispatcher)
