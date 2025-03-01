from django.test import TestCase
from ingredients.models import Ingredient


class IngredientModelTest(TestCase):
    def test_ingredient_creation(self):
        """ test create Ingredient """
        ingredient = Ingredient.objects.create(name="Tomato")
        self.assertEqual(ingredient.name, "Tomato")
