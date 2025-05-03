import pytest
from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize("name, price", [
        ("Black Bun", 100),
        ("White Bun", 150.5),
        ("Red Bun", 200)
    ])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", [
        ("Black Bun", 100),
        ("White Bun", 150.5),
        ("Red Bun", 200)
    ])
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
