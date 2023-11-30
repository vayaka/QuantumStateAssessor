from aiogram_dialog import Dialog

from bot.dialogs.opt_menu import windows


def bot_opt_menu():
    return [
        Dialog(
            windows.main_window(),
        ),
        Dialog(
            windows.types_window(),
            windows.structure_window(),
            windows.lambda_window(),
            windows.show_n_window(),
        )
    ]
