from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from recipes.models import Recipe

class RecipeModelTest(TestCase):
    def setUp(self):
        """ Build test user and recipe """
        self.user = User.objects.create_user(username="testuser", password="testpass")

        #  self.recipe use in all tests
        self.recipe = Recipe.objects.create(
            name="Test Recipe",
            cooking_time=20,
            ingredient_num=4,
            created_by=self.user
        )

    def test_recipe_creation(self):
        """ Test Recipe creation """
        self.assertEqual(self.recipe.name, "Test Recipe")
        self.assertEqual(self.recipe.calculate_difficulty, "Hard")  # difficulty correct test

    def test_get_absolute_url(self):
        """ Test get_absolute_url() """
        expected_url = reverse('recipes:recipe-detail', kwargs={'pk': self.recipe.pk})
        self.assertEqual(self.recipe.get_absolute_url(), expected_url)

    def test_recipe_detail_view(self):
        """ Test Recipe Detail View """
        response = self.client.get(reverse('recipes:recipe-detail', kwargs={'pk': self.recipe.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe.name)
        self.assertTemplateUsed(response, 'recipes/detail.html')
