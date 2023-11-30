from aiogram_dialog import DialogManager

from bot.misc.calculation import get_n


async def get_types(**kwargs):
    types = [
        ("Маломодовое", '1'),
        ("Одномодовое", '2'),
        ("Многомодовое", '3'),
    ]
    return {
        "types": types,
    }


def get_types_with_id(id: str, **kwargs):
    types = [
        ("Маломодовое", '1'),
        ("Одномодовое", '2'),
        ("Многомодовое", '3'),
    ]
    return [i for i, x in types if x == id][0]


async def get_structure(dialog_manager: DialogManager, **kwargs):
    structure = [("ERROR", "0")]
    match dialog_manager.dialog_data.get("type_opt_vol", 0):
        case "3":
            structure = [
                ("Односердцевинная", '1'),
            ]
            return {
                "structure": structure,
            }
        case "1" | "2":
            structure = [
                ("Односердцевинная", '1'),
                ("Многосердцевинная", '2'),
            ]
            return {
                "structure": structure,
            }
    return {
        "structure": structure,
    }


def get_structure_with_id(id: str, **kwargs):
    structure = [
        ("ERROR", "0"),
        ("Односердцевинная", '1'),
        ("Многосердцевинная", '2'),
    ]
    return [i for i, x in structure if x == id][0]


async def get_show_n_data(dialog_manager: DialogManager, **kwargs):
    result = get_n(
        type_vol=dialog_manager.dialog_data.get("type_opt_vol", ""),
        structure=dialog_manager.dialog_data.get("structure_opt_vol", ""),
        lambda_vol=dialog_manager.dialog_data.get("lambda_opt_vol", 0)
    )

    return {
        "result": round(result, 2),
        "type_vol": get_types_with_id(dialog_manager.dialog_data.get("type_opt_vol", "")),
        "structure": get_structure_with_id(dialog_manager.dialog_data.get("structure_opt_vol", "")),
        "lambda_vol": dialog_manager.dialog_data.get("lambda_opt_vol", "")
    }
