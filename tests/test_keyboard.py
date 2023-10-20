import pytest

from src.keyboard import Keyboard


@pytest.fixture
def get_kb():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    return kb


def test_keyboad(get_kb):

    assert str(get_kb.name) == "Dark Project KD87A"
    assert str(get_kb.language) == "EN"


def test_change_lang(get_kb):

    get_kb.change_lang()
    assert str(get_kb.language) == "RU"

    get_kb.change_lang()
    assert str(get_kb.language) == "EN"