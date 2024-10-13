# Req 3
import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.menu = self._load_menu_data(source_path)
        self.dishes = self._load_dishes(self.menu)

    def _load_menu_data(self, source_path: str) -> dict:
        dishes = {}
        with open(source_path, "r") as csv_file:
            data = csv.reader(csv_file, delimiter=",")
            for index, row in enumerate(data):
                if index == 0:
                    continue
                dish, price, ingredient, amount = row

                if dish not in dishes:
                    dishes[dish] = [price, []]

                dishes[dish][1].append((ingredient, amount))

        dishes_list = []
        for prato, dados in dishes.items():
            dishes_list.append([prato, dados[0], dados[1]])

        return dishes_list

    def _load_dishes(self, menu: list):
        dishes = set()
        for dish in menu:
            receita = Dish(dish[0], float(dish[1]))
            for ingredient in dish[2]:
                receita.add_ingredient_dependency(
                    Ingredient(ingredient[0]), int(ingredient[1])
                )
            dishes.add(receita)
        return dishes
