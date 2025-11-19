import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_currency(amount: float, from_currency: str, to_currency: str = "RUB") -> float:
    """Функция, обращающаяся к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли"""
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount
    }
    headers = {
        "apikey": API_KEY
    }
    response = requests.get(API_URL, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    if "result" in data:
        return float(data["result"])
    else:
        raise ValueError(f"Ошибка при конвертации: {data}")


def get_transaction_amount(transaction: dict) -> float:
    """Функция конвертации валюты из USD и EUR в рубли"""
    operation_amount = transaction.get("operationAmount")
    amount_str = operation_amount["amount"]
    amount = float(amount_str)
    currency_code = operation_amount["currency"]["code"].upper()

    if currency_code == "RUB":
        return amount
    elif currency_code in ["USD", "EUR"]:
        converted = convert_currency(amount, from_currency=currency_code)
        return converted
    else:
        raise ValueError(f"Неподдерживаемая валюта: {currency_code}")
