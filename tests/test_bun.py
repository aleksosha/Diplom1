import pytest
from praktikum.bun import Bun

@pytest.mark.parametrize("name, price", [
    ("Black Bun", 100),
    ("White Bun", 150.5),
    ("Red Bun", 200)
])
def test_bun_properties(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price
