from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:

    def test_buns_count(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_buns_have_names(self):
        db = Database()
        buns = db.available_buns()
        for bun in buns:
            assert bun.get_name() is not None

    def test_buns_have_positive_price(self):
        db = Database()
        buns = db.available_buns()
        for bun in buns:
            assert bun.get_price() > 0

    def test_ingredients_count(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_ingredients_have_valid_type(self):
        db = Database()
        ingredients = db.available_ingredients()
        for ingredient in ingredients:
            assert ingredient.get_type() in (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING)

    def test_ingredients_have_names(self):
        db = Database()
        ingredients = db.available_ingredients()
        for ingredient in ingredients:
            assert ingredient.get_name() is not None

    def test_ingredients_have_positive_price(self):
        db = Database()
        ingredients = db.available_ingredients()
        for ingredient in ingredients:
            assert ingredient.get_price() > 0
