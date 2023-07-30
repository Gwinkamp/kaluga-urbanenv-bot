import logging

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.answers import office_selection_answer_message, default_answer_message
from data.entities import User
from data.states import ChangeOffice

logger = logging.getLogger()


async def change_representative_office(message: types.Message, state: FSMContext):
    await state.set_state(ChangeOffice.WAITING_OFFICE_NUMBER.state)
    await message.answer(**office_selection_answer_message())


async def set_representative_office(message: types.Message, state: FSMContext):
    message_content = message.text.strip()
    if not message_content.isdigit() or int(message_content) < 1 or int(message_content) > 35:
        await message.answer(**office_selection_answer_message('Необходимо ввести целое число от 1 до 35'))
        return

    user_id = str(message.from_user.id)
    user = User.get_by_id(user_id)
    user.representative_office_number = int(message_content)
    user.save()

    logger.info(f'Пользователь {user_id} привязан к представительству №{message_content}')

    await message.answer(**default_answer_message('Представительство выбрано'))
    await state.finish()
