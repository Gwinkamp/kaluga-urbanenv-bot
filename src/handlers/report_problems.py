import logging
from typing import List

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.answers import (
    default_answer_message,
    problem_reporting_answer_message,
    problem_category_selection_answer_message
)
from data.categiries import ALLOWED_PROBLEM_CATEGORIES
from data.entities import Admin
from data.states import ReportProblem

logger = logging.getLogger()


async def report_problem(message: types.Message, state: FSMContext):
    await state.set_state(ReportProblem.WAITING_CATEGORY_SELECTION)
    await message.answer(**problem_reporting_answer_message())


async def select_category(message: types.Message, state: FSMContext):
    message_content = message.text.strip()

    if message_content not in ALLOWED_PROBLEM_CATEGORIES:
        await message.answer('Недопустимая категория')
        return

    await state.update_data(problem_category=message_content)
    await state.set_state(ReportProblem.WAITING_FOR_REPORT_DESCRIPTION.state)
    await message.answer(**problem_category_selection_answer_message())


async def report_description(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    messages = state_data.get('messages', [])
    messages.append(message)

    await state.update_data(messages=messages)


async def register_report(message: types.Message, state: FSMContext):
    await message.answer(**default_answer_message('Спасибо'))

    state_data = await state.get_data()
    problem_category = state_data['problem_category']
    report_messages = state_data['messages']

    for admin in Admin.select():
        await message.bot.send_message(admin.telegram_id, f'Поступило сообщение о проблеме на тему {problem_category}')
        await forward_messages_to_user(report_messages, admin.telegram_id)

    logger.info(f'Пользователь {message.from_user.id} сообщил о проблеме "{problem_category}"')
    await state.finish()


async def forward_messages_to_user(messages: List[types.Message], user_id: str):
    for message in messages:
        await message.forward(user_id)
