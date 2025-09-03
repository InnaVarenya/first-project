def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    clean_card_number = card_number.replace(" ", "")

    if len(clean_card_number) != 16:
        return "Введите корректный номер карты, состоящий из 16 цифр."

    part_1 = clean_card_number[0:4]
    part_2 = clean_card_number[4:6] + "**"
    part_3 = "****"
    part_4 = clean_card_number[12:]

    mask_card_number = f"{part_1} {part_2} {part_3} {part_4}"
    return mask_card_number


def get_mask_account(number_account: str) -> str:
    """Функция, которая маскирует номер банковского счета"""
    mask_account = f"**{number_account[-4:]}"
    return mask_account
