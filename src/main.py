import asyncio
import logging

from dependency_injector.providers import Configuration

from container import Container

logger = logging.getLogger()


def parse_admins(value: str):
    return [value.strip() for value in value.split(',')]


def read_config_from_env(config: Configuration):
    config.bot_token.from_env('BOT_TOKEN', as_=str, required=True)
    config.admins.from_env('BOT_ADMINS', as_=parse_admins, required=True)
    config.db_connection_string.from_env('DB_CONNECTION_STRING', as_=str, required=True, default='sqlite:///local.db')


if __name__ == '__main__':
    container = Container()

    read_config_from_env(container.config)
    container.init_resources()
    dispatcher = container.dispatcher()

    logger.info('Старт бота')
    asyncio.run(dispatcher.start_polling())
