from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_card_or_account: str) -> str:
    """Функция, обррабатывающая информацию о картах и о счетах"""
    number = ""
    letter = ""

    for symbol in number_card_or_account:
        if symbol.isdigit():
            number += symbol
        elif symbol.isalpha():
            letter += symbol

    if len(number) == 16:
        return letter + " " + get_mask_card_number(number)
    else:
        return letter + " " + get_mask_account(number)


def get_date(str_date: str) -> str:
    """Функция, форматирующая дату в корректный формат"""
    dd = str_date[8:10]
    mm = str_date[5:7]
    gggg = str_date[0:4]
    return f"{dd}.{mm}.{gggg}"
