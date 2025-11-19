import json
import logging
from typing import Any, Dict, List

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("logs/utils.log", encoding="utf-8")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def data_fin_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Функция, принимающая на вход путь до JSON-файла,
    возвращающая список словарей с данными о финансовых транзакциях"""
    logger.info(f"Попытка открыть файл: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f"Данные успешно считаны из файла: {file_path}")
                return data
            else:
                logger.warning(f"Данные из файла {file_path} не являются списком.")
                return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {file_path}")
        return []
