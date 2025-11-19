import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number_card, expected", [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234 5678 9012 3456", "1234 56** **** 3456"),
        ("12345", "Введите корректный номер карты, состоящий из 16 цифр."),
        ("1234567890123456789", "Введите корректный номер карты, состоящий из 16 цифр."),
        (" 1234567890123456 ", "1234 56** **** 3456"),
        ("", "Введите корректный номер карты, состоящий из 16 цифр.")
    ]
)
def test_get_mask_card_number(number_card: str, expected: str) -> None:
    assert get_mask_card_number(number_card) == expected


@pytest.mark.parametrize(
    "number_account, expected", [
        ("124543545", "**3545"),
        ("1233985394857", "**4857"),
        ("5", "**5"),
        ("", "**")
    ]
)
def test_get_mask_account(number_account: str, expected: str) -> None:
    assert get_mask_account(number_account) == expected
