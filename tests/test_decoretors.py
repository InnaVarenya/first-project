import pytest

from src.decorators import log


@log()
def func_sum(a, b):
    return a + b


@log()
def func_error(x):
    raise ValueError("Test error")


def test_log_success(capsys):
    result = func_sum(2, 3)
    captured = capsys.readouterr()
    assert result == 5
    assert "func_sum ok" in captured.out


def test_log_error(capsys):
    with pytest.raises(ValueError):
        func_error(10)
    captured = capsys.readouterr()
    assert "func_error error: ValueError. Inputs: ((10,), {})" in captured.out
