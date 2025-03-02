from django.test import TestCase

from django.test import TestCase
from django.contrib.auth.models import User
from recipes.models import Recipe


class RecipeModelTest(TestCase):
    def setUp(self):
        """ build test user """
        self.user = User.objects.create_user(
            username="testuser", password="testpass")

    def test_recipe_creation(self):
        """ test create Recipe """
        recipe = Recipe.objects.create(
            name="Test Recipe",
            cooking_time=20,
            ingredient_num=4,
            created_by=self.user
        )
        recipe.save()
        self.assertEqual(recipe.name, "Test Recipe")
        self.assertEqual(recipe.calculate_difficulty, "Hard")
