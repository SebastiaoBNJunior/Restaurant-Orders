from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_1 = Ingredient("carne")
    ingredient_2 = Ingredient("carne")
    ingredient_3 = Ingredient("queijo provolone")
    assert hash(ingredient_1) == hash(ingredient_2)
    assert hash(ingredient_1) != hash(ingredient_3)
    assert (ingredient_1 == ingredient_2) is True
    assert (ingredient_1 == ingredient_3) is False
    assert repr(ingredient_1) == "Ingredient('carne')"
    assert ingredient_3.name == "queijo provolone"
    assert (ingredient_1.restrictions) == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }
