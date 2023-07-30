import logging

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.answers import (
    starting_answer_message,
    default_answer_message
)
from data.entities import User

logger = logging.getLogger()


async def start(message: types.Message, state: FSMContext):
    await state.finish()

    user_id = str(message.from_user.id)
    user = User.get_or_none(User.telegram_id == user_id)

    if user is None:
        User.create(
            telegram_id=user_id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            full_name=message.from_user.full_name,
            mention=message.from_user.mention,
            username=message.from_user.username,
            url=message.from_user.url,
            is_bot=message.from_user.is_bot,
            representative_office_number=None
        )
        logger.info(f'Пользователь {user_id} подключился к боту')

        await message.answer(**starting_answer_message())
        return

    if user.representative_office_number is None:
        await message.answer(**starting_answer_message('Для дальнейшей работы необходимо выбрать представительство'))
        return

    await message.answer(**default_answer_message())


async def cancel(message: types.Message, state: FSMContext):
    await state.finish()

    user_id = str(message.from_user.id)
    user = User.get_or_none(User.telegram_id == user_id)

    if user.representative_office_number is None:
        await message.answer(**starting_answer_message('Для дальнейшей работы необходимо выбрать представительство'))
        return

    await message.answer(**default_answer_message('Действие отменено'))
