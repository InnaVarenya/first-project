import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

@pytest.fixture
def transactions_data():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 142264269,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]


def test_filter_by_currency(transactions_data):
    result = list(filter_by_currency(transactions_data, "USD"))
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in result)
    assert len(result) == 2


def test_filter_by_currency_rub(transactions_data):
    result = list(filter_by_currency(transactions_data, "RUB"))
    assert all(t["operationAmount"]["currency"]["code"] == "RUB" for t in result)
    assert len(result) == 1


def test_transaction_descriptions(transactions_data):
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту"
    ]
    result_descriptions = list(transaction_descriptions(transactions_data))
    assert result_descriptions == expected_descriptions


@pytest.mark.parametrize("start, end, expected", [
    (0, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (77, 78, ["0000 0000 0000 0077", "0000 0000 0000 0078"]),
    (0, 0, [])
])
def test_card_number_generator(start, end, expected):
    result = list(card_number_generator(start, end))
    assert result == expected
