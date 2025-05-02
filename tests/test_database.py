from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

def test_available_buns():
    db = Database()
    buns = db.available_buns()
    assert len(buns) == 3
    for bun in buns:
        assert bun.get_name() is not None
        assert bun.get_price() > 0

def test_available_ingredients():
    db = Database()
    ingredients = db.available_ingredients()
    assert len(ingredients) == 6
    for ingredient in ingredients:
        assert ingredient.get_type() in (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING)
        assert ingredient.get_name() is not None
        assert ingredient.get_price() > 0
