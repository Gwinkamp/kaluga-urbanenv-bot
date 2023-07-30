from aiogram.dispatcher.filters.state import State, StatesGroup


class ChangeOffice(StatesGroup):
    # Ожидание ввода номера представительства
    WAITING_OFFICE_NUMBER = State()


class ReportProblem(StatesGroup):
    """Состояния доклада о проблеме"""

    # Ожидание выбора категории проблемы
    WAITING_CATEGORY_SELECTION = State()

    # Ожидание описания проблемы
    WAITING_FOR_REPORT_DESCRIPTION = State()
