"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture
def get_item():
    item1 = Item("Ноутбук", 20000, 5)
    return item1


def test_calculate_total_price(get_item):
    assert get_item.calculate_total_price() == 100000


def test_apply_discount(get_item):
    Item.pay_rate = 0.85
    assert get_item.apply_discount() == 17000


def test_name(get_item):
    assert get_item.name == "Ноутбук"

    get_item.name = "СуперСмартфон"
    assert get_item.name == "СуперСмарт"

    get_item.name = "Смарт"
    assert get_item.name == "Смарт"
