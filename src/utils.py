import json
from typing import Any, Dict, List


def data_fin_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Функция, принимающая на вход путь до JSON-файла,
    возвращающая список словарей с данными о финансовых транзакциях"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if type(data) == list:
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
