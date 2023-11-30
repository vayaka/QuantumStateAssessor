from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class OptVol(CallbackData):
    """Optical fiber type"""
    small_mode: int
    one_mode: int
    more_mode: int


keyboard_opt_vol = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Маломодное", callback_data=OptVol(one_mode=0, small_mode=1, more_mode=0).pack()),
    InlineKeyboardButton(text="Одномодовое", callback_data=OptVol(one_mode=1, small_mode=0, more_mode=0).pack()),
    InlineKeyboardButton(text="Многомодовое", callback_data=OptVol(one_mode=0, small_mode=0, more_mode=1).pack())]])
