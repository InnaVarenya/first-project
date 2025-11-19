from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def executed_canceled_items() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 4, "state": "CANCELED"},
    ]


@pytest.fixture
def all_canceled_items() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "state": "CANCELED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "CANCELED"},
        {"id": 4, "state": "CANCELED"},
    ]


@pytest.fixture
def empty_dict_item() -> List[Dict[str, Any]]:
    return [{}]


@pytest.fixture
def date_items() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "date": "2025-09-20T12:00:00.000000"},
        {"id": 2, "date": "2024-01-15T08:30:00.123456"},
        {"id": 3, "date": "2025-09-20T12:00:00.000000"},
    ]


@pytest.fixture
def date_items_duplicated() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "date": "2025-09-20T12:00:00.000000"},
        {"id": 2, "date": "2024-01-15T08:30:00.123456"},
        {"id": 3, "date": "2025-09-20T12:00:00.000000"},
    ]


@pytest.fixture
def date_items_year_start() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "date": "2025-01-01T00:00:00.000000"},
        {"id": 2, "date": "2025-01-01T00:00:00.000000"},
        {"id": 3, "date": "2024-12-31T23:59:59.999999"},
    ]


@pytest.fixture
def date_items_all_same() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "date": "2025-01-01T00:00:00.000000"},
        {"id": 2, "date": "2025-01-01T00:00:00.000000"},
        {"id": 3, "date": "2025-01-01T00:00:00.000000"},
    ]


def test_filter_by_state_executed(executed_canceled_items: List[Dict[str, Any]]) -> None:
    expected = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 3, "state": "EXECUTED"},
    ]
    assert filter_by_state(executed_canceled_items) == expected


def test_filter_by_state_all_canceled(all_canceled_items: List[Dict[str, Any]]) -> None:
    expected: List = []
    assert filter_by_state(all_canceled_items) == expected


def test_filter_by_state_empty_dict(empty_dict_item: List[Dict[str, Any]]) -> None:
    expected: List = []
    assert filter_by_state(empty_dict_item) == expected


def test_sort_by_date_normal(date_items: List[Dict[str, Any]]) -> None:
    expected = [
        {"id": 1, "date": "2025-09-20T12:00:00.000000"},
        {"id": 3, "date": "2025-09-20T12:00:00.000000"},
        {"id": 2, "date": "2024-01-15T08:30:00.123456"},
    ]
    assert sort_by_date(date_items) == expected


def test_sort_by_date_duplicated(date_items_duplicated: List[Dict[str, Any]]) -> None:
    expected = [
        {"id": 1, "date": "2025-09-20T12:00:00.000000"},
        {"id": 3, "date": "2025-09-20T12:00:00.000000"},
        {"id": 2, "date": "2024-01-15T08:30:00.123456"},
    ]
    assert sort_by_date(date_items_duplicated) == expected


def test_sort_by_date_year_start(date_items_year_start: List[Dict[str, Any]]) -> None:
    expected = [
        {"id": 1, "date": "2025-01-01T00:00:00.000000"},
        {"id": 2, "date": "2025-01-01T00:00:00.000000"},
        {"id": 3, "date": "2024-12-31T23:59:59.999999"},
    ]
    assert sort_by_date(date_items_year_start) == expected


def test_sort_by_date_all_same(date_items_all_same: List[Dict[str, Any]]) -> None:
    expected = [
        {"id": 1, "date": "2025-01-01T00:00:00.000000"},
        {"id": 2, "date": "2025-01-01T00:00:00.000000"},
        {"id": 3, "date": "2025-01-01T00:00:00.000000"},
    ]
    assert sort_by_date(date_items_all_same) == expected


def test_sort_by_date_ascending(date_items: List[Dict[str, Any]]) -> None:
    expected = [
        {"id": 2, "date": "2024-01-15T08:30:00.123456"},
        {"id": 1, "date": "2025-09-20T12:00:00.000000"},
        {"id": 3, "date": "2025-09-20T12:00:00.000000"},
    ]
    assert sort_by_date(date_items, reverse=False) == expected
