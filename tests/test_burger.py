from unittest.mock import MagicMock
from praktikum.burger import Burger

class TestBurger:

    def test_set_buns(self):
        bun = MagicMock()
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        ingredient = MagicMock()
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient(self):
        ingredient1 = MagicMock()
        ingredient2 = MagicMock()
        burger = Burger()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredient2]

    def test_move_ingredient(self):
        ingredient1 = MagicMock()
        ingredient2 = MagicMock()
        burger = Burger()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient2, ingredient1]

    def test_get_price(self):
        bun = MagicMock()
        bun.get_price.return_value = 100
        ingredient1 = MagicMock()
        ingredient1.get_price.return_value = 50
        ingredient2 = MagicMock()
        ingredient2.get_price.return_value = 25
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        expected_price = 100 * 2 + 50 + 25
        assert burger.get_price() == expected_price

    def test_receipt_contains_bun_name(self):
        bun = MagicMock()
        bun.get_name.return_value = "Test Bun"
        bun.get_price.return_value = 100
        ingredient = MagicMock()
        ingredient.get_type.return_value = "SAUCE"
        ingredient.get_name.return_value = "Test Sauce"
        ingredient.get_price.return_value = 50

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()

        assert "(==== Test Bun ====)" in receipt

    def test_receipt_contains_ingredient(self):
        bun = MagicMock()
        bun.get_name.return_value = "Test Bun"
        bun.get_price.return_value = 100
        ingredient = MagicMock()
        ingredient.get_type.return_value = "SAUCE"
        ingredient.get_name.return_value = "Test Sauce"
        ingredient.get_price.return_value = 50

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()

        assert "= sauce Test Sauce =" in receipt

    def test_receipt_contains_total_price(self):
        bun = MagicMock()
        bun.get_name.return_value = "Test Bun"
        bun.get_price.return_value = 100
        ingredient = MagicMock()
        ingredient.get_type.return_value = "SAUCE"
        ingredient.get_name.return_value = "Test Sauce"
        ingredient.get_price.return_value = 50

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()

        assert "Price: 250" in receipt
