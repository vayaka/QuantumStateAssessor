from aiogram import Router, types
from aiogram.filters import Command
from aiogram_dialog import DialogManager

from bot.dialogs.opt_menu.states import MainMenu

user_router = Router()


@user_router.message(Command('evaluate'))
async def cmd_evaluate(message: types.Message, dialog_manager: DialogManager):
    await dialog_manager.start(MainMenu.main_menu)
