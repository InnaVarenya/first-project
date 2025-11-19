import json
from unittest.mock import mock_open, patch

from src.utils import data_fin_transactions


def test_valid_json_list():
    mock_data = json.dumps([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = data_fin_transactions("fake_path.json")
        assert isinstance(result, list)
        assert result == [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]


def test_json_not_list():
    mock_data = json.dumps({"key": "value"})
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = data_fin_transactions("fake_path.json")
        assert result == []


def test_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = data_fin_transactions("wrong_path.json")
        assert result == []


def test_json_decode_error():
    with patch("builtins.open", mock_open(read_data="{bad json")):
        result = data_fin_transactions("bad_json.json")
        assert result == []
