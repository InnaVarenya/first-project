import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card, expected", [
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 12314567890123456", "Счет **3456"),
        ("Visa Platinum 7859456321545954", "Visa Platinum 7859 45** **** 5954"),
        ("Mir 1234567890123456", "Mir 1234 56** **** 3456"),
        ("Maestro 1234567890123456789", "Maestro **6789")
    ]
)
def test_mask_account_card(card: str, expected: str) -> None:
    assert mask_account_card(card) == expected


@pytest.mark.parametrize(
    "date, expected", [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2018-09-14T03:46:10.583109", "14.09.2018"),
        ("", "Некорректный формат даты"),
        ("1255468695", "Некорректный формат даты")
    ]
)
def test_get_date(date: str, expected: str) -> None:
    assert get_date(date) == expected
