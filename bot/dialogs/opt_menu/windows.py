import logging
import operator

from aiogram_dialog import Window, Data, DialogManager, StartMode
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Column, Select, Row, Button, Start, Cancel, Back, SwitchTo
from aiogram_dialog.widgets.text import Const, Format
from typing import Any

from .getters import get_types, get_structure, get_show_n_data
from .selected import on_type_selected, on_structure_selected, on_lambda_entered
from .states import FormOpt, MainMenu


def main_window():
    return Window(
        Const("""🔍 Начнем Оценку НТС для Вашей Квантовой Системы 🔍\n
Пожалуйста, ответьте на несколько вопросов и выберите тип вашего оборудования. Ваш выбор поможет нам точно оценить состояние и потребности системы.
В конце вы получите оценку N.\n
Если нужна помощь, введите /help.\n
Готовы? Давайте начнем с первого вопроса!
"""),
        Column(
            Start(Const("Начать оценку"), id="start_opt", state=FormOpt.choose_opt_type),
            Cancel(Const("Отмена"), id="cancel_opt")
        ),
        state=MainMenu.main_menu
    )


def types_window():
    return Window(
        Const("Выберите тип оптического волокна:"),
        Column(
            Select(
                Format("{item[0]}"),
                id="opts_vol",
                item_id_getter=operator.itemgetter(1),
                items="types",
                on_click=on_type_selected
            )
        ),
        state=FormOpt.choose_opt_type,
        getter=get_types
    )


def structure_window():
    return Window(
        Const("Выберите структуру оптического волокна:"),
        Column(
            Select(
                Format("{item[0]}"),
                id="opts_vol",
                item_id_getter=operator.itemgetter(1),
                items="structure",
                on_click=on_structure_selected
            )
        ),
        state=FormOpt.choose_opt_structure,
        getter=get_structure
    )


def lambda_window():
    return Window(
        Const("Введите длину волны (нм):"),
        TextInput(
            id="enter_lambda",
            on_success=on_lambda_entered
        ),
        state=FormOpt.choose_opt_lambda
    )


def show_n_window():
    return Window(
        Format("""📊Результат оценки:📊\n
Тип оптического волокна: {type_vol}
Структура оптического волокна: {structure}
Длина волны: {lambda_vol} нм\n
Оценка N = {result}"""),
        Row(
            SwitchTo(Const("Начать оценку сначала"), id="start_opt", state=FormOpt.choose_opt_type),
            Back(Const("Ввести новое значение ДВ"), id="cancel_lambda")
        ),
        Cancel(Const("Вернуться в главное меню"), id="cancel_opt"),
        getter=get_show_n_data,
        state=FormOpt.show_n
    )

# async def on_process_result(start_data: Data, result: Any, dialog_manager: DialogManager, **kwargs):
#     logging.info(f"{result=}")
