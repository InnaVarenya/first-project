from unittest.mock import Mock, patch

from src.external_api import convert_currency, get_transaction_amount


def test_convert_currency_success():
    with patch("src.external_api.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json.return_value = {"result": 1234.56}
        mock_get.return_value = mock_response

        result = convert_currency(100, "USD")
        assert result == 1234.56


def test_convert_currency_failure():
    with patch("src.external_api.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json.return_value = {"error": "что-то пошло не так"}
        mock_get.return_value = mock_response

        try:
            convert_currency(100, "USD")
            assert False, "Ожидалась ошибка, но она не возникла."
        except ValueError:
            pass


def test_get_transaction_amount_rub():
    transaction = {
        "operationAmount": {
            "amount": "500",
            "currency": {"code": "RUB"}
        }
    }
    result = get_transaction_amount(transaction)
    assert result == 500


@patch("src.external_api.convert_currency")
def test_get_transaction_amount_usd(mock_convert):
    mock_convert.return_value = 2000
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }
    result = get_transaction_amount(transaction)
    assert result == 2000
    assert mock_convert.called


def test_unsupported_currency():
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "JPY"}
        }
    }
    try:
        get_transaction_amount(transaction)
        assert False, "Ожидалась ошибка, но она не возникла."
    except ValueError:
        pass
