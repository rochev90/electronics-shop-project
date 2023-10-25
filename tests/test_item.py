"""Здесь надо написать тесты с использованием pytest для модуля item."""

import csv
from src.ExeptionsErrors import InstantiateCSVError
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def get_item():
    item1 = Item("Ноутбук", 20000, 5)
    return item1


def test_repr(get_item):
    assert get_item.__repr__() == "Item('Ноутбук', 20000, 5)"


def test_str(get_item):
    assert get_item.__str__() == 'Ноутбук'


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


def test_instantiate_from_csv():
    """ Отсутствие файла"""
    with pytest.raises(FileNotFoundError):
        with open('../src/itemss.csv', newline='') as file:
            reader = csv.DictReader(file)


def test_instantiate_from_csv2():
    """ Повреждение файла"""
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('../tests/test_item.csv')
        assert "Файл ../tests/test_item.csv поврежден."