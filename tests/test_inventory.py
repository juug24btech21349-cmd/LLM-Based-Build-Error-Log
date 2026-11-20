import pytest

from src.inventory import Inventory


def test_add_stock():
    inventory = Inventory()
    inventory.add_stock("pen", 5)
    inventory.add_stock("pen", 3)
    assert inventory.stock["pen"] == 8


def test_remove_stock():
    inventory = Inventory()
    inventory.add_stock("pen", 5)
    inventory.remove_stock("pen", 2)
    assert inventory.stock["pen"] == 3


def test_remove_too_much_raises_value_error():
    inventory = Inventory()
    inventory.add_stock("pen", 2)
    with pytest.raises(ValueError, match="not enough stock"):
        inventory.remove_stock("pen", 3)
