from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager

from bot.dialogs.opt_menu.states import FormOpt, MainMenu

user_router = Router()


# @user_router.message(Command('evaluate'))
# async def cmd_evaluate(message: types.Message, state: FSMContext):
#     await message.answer("""🔍 Начнем Оценку НТС для Вашей Квантовой Системы 🔍\n
# Пожалуйста, ответьте на несколько вопросов и выберите тип вашего оборудования. Ваш выбор поможет нам точно оценить состояние и потребности системы.
# В конце вы получите оценку N.\n
# Если нужна помощь, введите /help.\n
# Готовы? Давайте начнем с первого вопроса!
# """)
#     await message.answer("Выбери оптическое волокно:", reply_markup=keyboard_opt_vol)
#     await state.set_state(FormOpt.choose_opt_vol)

@user_router.message(Command('evaluate'))
async def cmd_evaluate(message: types.Message, dialog_manager: DialogManager):
    #     await message.answer("""🔍 Начнем Оценку НТС для Вашей Квантовой Системы 🔍\n
    # Пожалуйста, ответьте на несколько вопросов и выберите тип вашего оборудования. Ваш выбор поможет нам точно оценить состояние и потребности системы.
    # В конце вы получите оценку N.\n
    # Если нужна помощь, введите /help.\n
    # Готовы? Давайте начнем с первого вопроса!
    # """)
    await dialog_manager.start(MainMenu.main_menu)


async def cmd_lambda_get(message: types.Message):
    return message.text
