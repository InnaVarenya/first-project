def filter_by_currency(transactions, currency_code):
    """Функция, выдающая транзакции, где валюта операции соответствует заданной"""
    for t in transactions:
        if t.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield t


def transaction_descriptions(transactions):
    """Функция, принимающая список словарей и возвращающая описание каждой операции по очереди"""
    for tx in transactions:
        yield tx.get("description", "")


def card_number_generator(start, end):
    """Генератор, выдающий номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    if start == 0:
        start = 1
    for num in range(start, end + 1):
        card_str = str(num).zfill(16)
        card_number = card_str[0:4] + " " + card_str[4:8] + " " + card_str[8:12] + " " + card_str[12:16]
        yield card_number
