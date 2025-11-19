import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    logger.debug(f"Получен номер карты для маскировки: {card_number}")
    clean_card_number = card_number.replace(" ", "")
    logger.debug(f"Обработанный номер карты без пробелов: {clean_card_number}")

    if len(clean_card_number) != 16:
        logger.error(f"Некорректная длина номера карты: {len(clean_card_number)}")
        return "Введите корректный номер карты, состоящий из 16 цифр."

    part_1 = clean_card_number[0:4]
    part_2 = clean_card_number[4:6] + "**"
    part_3 = "****"
    part_4 = clean_card_number[12:]
    masked_card = f"{part_1} {part_2} {part_3} {part_4}"

    logger.info(f"Маскированный номер карты: {masked_card}")
    return masked_card


def get_mask_account(number_account: str) -> str:
    """Функция, которая маскирует номер банковского счета"""
    logger.debug(f"Получен номер счета для маскировки: {number_account}")
    if len(number_account) < 4:
        logger.error(f"Недостаточная длина номера счета: {len(number_account)}")
        return "Некорректный номер счета."
    mask_account = f"**{number_account[-4:]}"
    logger.info(f"Маскированный номер счета: {mask_account}")
    return mask_account
