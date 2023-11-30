from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    """User state"""
    # States
    choose_opt_vol = State()
    choose_opt_type = State()
    choose_opt_lambda = State()
    # show_n = State()
