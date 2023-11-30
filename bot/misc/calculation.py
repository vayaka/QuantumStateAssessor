def get_formula_150(base_n: int, add_n: int, lambda_vol: int) -> float:
    return (base_n + add_n) + (lambda_vol / 150)


def get_formula_300(base_n: int, add_n: int, lambda_vol: int) -> float:
    return (base_n + add_n) + (lambda_vol / 300)


def get_n(type_vol: str = None, structure: str = None, lambda_vol: int = None) -> float:
    if not type_vol or not structure or not lambda_vol:
        return 0
    if lambda_vol is not None:
        lambda_vol = int(lambda_vol)

    match (type_vol, structure):
        case "1", _:
            return 5
        case "2", "1":
            return get_formula_150(10, 5, lambda_vol)
        case "2", "2":
            return get_formula_150(10, 15, lambda_vol)
        case "3", "1" if lambda_vol <= 1300:
            return get_formula_300(1, 0, lambda_vol)
        case "3", "1" if lambda_vol >= 1300:
            return get_formula_150(1, 0, lambda_vol)
        case _:
            return 0


if __name__ == '__main__':
    print(round(get_n(type_vol="3", structure="1", lambda_vol=900), 1))
