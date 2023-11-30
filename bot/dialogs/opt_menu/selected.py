import logging
from typing import Any

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager

from bot.dialogs.opt_menu.states import FormOpt


async def on_type_selected(c: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(type_opt_vol=item_id)
    await manager.switch_to(FormOpt.choose_opt_structure)


async def on_structure_selected(c: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(structure_opt_vol=item_id)
    await manager.switch_to(FormOpt.choose_opt_lambda)


async def on_lambda_entered(m: Message, widget: Any, manager: DialogManager, lambda_int: str):
    ctx = manager.current_context()
    if not lambda_int.isdigit():
        await m.answer("Введите число!")
        return
    if not 850 <= int(lambda_int) <= 1700:
        await m.answer("Введите число в границах 850 <-> 1700 (нм)!")
        return
    ctx.dialog_data.update(lambda_opt_vol=lambda_int)
    await manager.switch_to(FormOpt.show_n)
