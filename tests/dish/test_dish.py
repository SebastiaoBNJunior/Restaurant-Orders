from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    lasanha = Dish("lasanha", 80)
    outra_lasanha = Dish("lasanha", 80)
    file_com_fritas = Dish("file_com_fritas", 49.90)

    assert lasanha.name == "lasanha"
    assert lasanha.price == 80.00
    assert hash(lasanha) == hash(outra_lasanha)
    assert hash(lasanha) != hash(file_com_fritas)
    assert lasanha == outra_lasanha
    assert repr(lasanha) == "Dish('lasanha', R$80.00)"

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("file_com_fritas", "30")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("file_com_fritas", -30)

    ingredient_1 = Ingredient("carne")
    ingredient_2 = Ingredient("massa de lasanha")
    lasanha.add_ingredient_dependency(ingredient_1, 1)
    lasanha.add_ingredient_dependency(ingredient_2, 2)

    assert lasanha.get_ingredients() == {
        Ingredient("carne"),
        Ingredient("massa de lasanha"),
    }

    assert lasanha.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.LACTOSE,
        Restriction.GLUTEN,
    }
