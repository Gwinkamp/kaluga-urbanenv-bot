from aiogram import types

from data.categiries import ALLOWED_PROBLEM_CATEGORIES

START_ANSWER_MESSAGE_TEXT = (
    'Привет! '
    'Сюда ты можешь направить городскую проблему, '
    'находящейся на территории твоего представительства.'
)


def starting_answer_message(text: str = START_ANSWER_MESSAGE_TEXT + ' Для начала необходимо выбрать представительство'):
    return {
        'text': text,
        'reply_markup': types.ReplyKeyboardMarkup([
            [types.KeyboardButton('Выбрать представительство')]
        ], resize_keyboard=True)
    }


def default_answer_message(text: str = START_ANSWER_MESSAGE_TEXT):
    return {
        'text': text,
        'reply_markup': types.ReplyKeyboardMarkup([
            [
                types.KeyboardButton('Сменить представительство'),
                types.KeyboardButton('Сообщить о проблеме')
            ]
        ], resize_keyboard=True)
    }


def office_selection_answer_message(text: str = 'Выберите номер представительства'):
    markup = [
        [
            types.KeyboardButton(str(row + 5 * column)) for row in range(1, 6)
        ] for column in range(7)
    ]
    markup.append([types.KeyboardButton('Отмена')])
    return {
        'text': text,
        'reply_markup': types.ReplyKeyboardMarkup(markup, resize_keyboard=True)
    }


def problem_reporting_answer_message(text: str = 'Выберите категорию'):
    markup = [ALLOWED_PROBLEM_CATEGORIES[i:i + 2] for i in range(0, len(ALLOWED_PROBLEM_CATEGORIES), 2)]
    markup.append([types.KeyboardButton('Отмена')])
    return {
        'text': text,
        'reply_markup': types.ReplyKeyboardMarkup(markup, resize_keyboard=True)
    }


def problem_category_selection_answer_message():
    return {
        'text': 'Опишите проблему и прикрепите фотографии',
        'reply_markup': types.ReplyKeyboardMarkup([
            [types.KeyboardButton('Сохранить отчет'), types.KeyboardButton('Отмена')]
        ], resize_keyboard=True)
    }
