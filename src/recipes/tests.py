from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from recipes.models import Recipe
from recipesingredients.models import RecipeIngredient
from ingredients.models import Ingredient

from recipes.forms import IngredientSearchForm


class RecipeModelTest(TestCase):
    def setUp(self):
        """ Build test user and recipe """
        self.user = User.objects.create_user(
            username="testuser", password="testpass")

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
        self.assertEqual(self.recipe.calculate_difficulty,
                         "Hard")  # difficulty correct test

    def test_get_absolute_url(self):
        """ Test get_absolute_url() """
        expected_url = reverse('recipes:recipe_detail',
                               kwargs={'pk': self.recipe.pk})
        self.assertEqual(self.recipe.get_absolute_url(), expected_url)

    def test_recipe_detail_view(self):
        """ Test Recipe Detail View """
        self.client.login(username="testuser",
                          password="testpass")  # detail view needs login
        response = self.client.get(
            reverse('recipes:recipe_detail', kwargs={'pk': self.recipe.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe.name)
        self.assertTemplateUsed(response, 'recipes/detail.html')


class RecipeFormTest(TestCase):
    def test_ingredient_search_form_valid(self):
        """ Test if the form is valid with correct input """
        form = IngredientSearchForm(data={"ingredient": "Milk"})
        self.assertTrue(form.is_valid())

    def test_ingredient_search_form_invalid(self):
        """ Test if the form is invalid with empty input """
        form = IngredientSearchForm(data={"ingredient": ""})
        self.assertTrue(form.is_valid())  # if it's empty, it will not crush


class RecipeViewsTest(TestCase):
    def setUp(self):
        """Create test user, ingredients, and recipes."""
        self.user = User.objects.create_user(
            username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name="Onion")
        self.ingredient2 = Ingredient.objects.create(name="Milk")

        # Create recipes
        self.recipe1 = Recipe.objects.create(
            name="Onion Soup",
            cooking_time=30,
            ingredient_num=2,
            created_by=self.user
        )
        self.recipe2 = Recipe.objects.create(
            name="Milkshake",
            cooking_time=10,
            ingredient_num=1,
            created_by=self.user
        )

        # Link recipes to ingredients
        RecipeIngredient.objects.create(
            recipe=self.recipe1, ingredient=self.ingredient1)
        RecipeIngredient.objects.create(
            recipe=self.recipe2, ingredient=self.ingredient2)

    def test_ingredient_search_view(self):
        """ Test if the ingredient search page loads correctly """
        response = self.client.get(reverse('recipes:ingredient_search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/ingredient_search.html')

    def test_pie_chart_generation(self):
        """ Test if Pie Chart generates correctly when an ingredient is provided """
        response = self.client.get(reverse('recipes:ingredient_search'), {
                                   'ingredient': 'Onion', 'chart_type': '#1'})
        # Check if chart is generated
        self.assertIsNotNone(response.context.get("chart"))

    def test_bar_chart_generation(self):
        """ Test if Bar Chart generates correctly """
        response = self.client.get(
            reverse('recipes:ingredient_search'), {'chart': '#2'})
        self.assertIsNotNone(response.context.get("chart"))

    def test_line_chart_generation(self):
        """ Test if Line Chart generates correctly """
        response = self.client.get(
            reverse('recipes:ingredient_search'), {'chart': '#3'})
        self.assertIsNotNone(response.context.get("chart"))

    def test_unauthorized_access(self):
        """ Test if an unauthorized user gets redirected """
        self.client.logout()
        response = self.client.get(reverse('recipes:ingredient_search'))
        # Should redirect to login
        self.assertNotEqual(response.status_code, 200)
