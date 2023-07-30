from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text, CommandStart
from aiogram.types import ContentType

from data.states import ChangeOffice, ReportProblem
from .change_office import set_representative_office, change_representative_office
from .common import start, cancel
from .report_problems import report_problem, select_category, report_description, register_report


def register_handlers(dispatcher: Dispatcher):
    # common
    dispatcher.register_message_handler(start, CommandStart(), state='*')
    dispatcher.register_message_handler(cancel, Text(equals='Отмена', ignore_case=True), state='*')

    # change office
    dispatcher.register_message_handler(
        change_representative_office,
        Text(equals=['Выбрать представительство', 'Сменить представительство'], ignore_case=True),
        content_types=[ContentType.TEXT],
        state='*'
    )
    dispatcher.register_message_handler(
        set_representative_office,
        content_types=[ContentType.TEXT],
        state=ChangeOffice.WAITING_OFFICE_NUMBER)

    # report problem
    dispatcher.register_message_handler(
        report_problem,
        Text(equals='Сообщить о проблеме', ignore_case=True),
        content_types=[ContentType.TEXT],
        state='*'
    )
    dispatcher.register_message_handler(
        select_category,
        content_types=[ContentType.TEXT],
        state=ReportProblem.WAITING_CATEGORY_SELECTION
    )
    dispatcher.register_message_handler(
        register_report,
        Text(equals='Сохранить отчет', ignore_case=True),
        content_types=[ContentType.TEXT],
        state=ReportProblem.WAITING_FOR_REPORT_DESCRIPTION
    )
    dispatcher.register_message_handler(
        report_description,
        content_types=[ContentType.ANY],
        state=ReportProblem.WAITING_FOR_REPORT_DESCRIPTION
    )
