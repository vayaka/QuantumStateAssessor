from aiogram.fsm.state import StatesGroup, State


class MainMenu(StatesGroup):
    main_menu = State()


class FormOpt(StatesGroup):
    # States
    choose_opt_type = State()
    choose_opt_structure = State()
    choose_opt_lambda = State()
    show_n = State()
