from django.test import TestCase
from django.urls import reverse
from ingredients.models import Ingredient


class IngredientModelTest(TestCase):

    def setUp(self):
        self.ingredient = Ingredient.objects.create(name="Sugar")

    def test_ingredient_creation(self):
        """ test create Ingredient """
        ingredient = Ingredient.objects.create(name="Tomato")
        self.assertEqual(ingredient.name, "Tomato")

    def test_get_absolute_url(self):
        expected_url = reverse('ingredients:ingredient-detail', kwargs={'pk': self.ingredient.pk})
        self.assertEqual(self.ingredient.get_absolute_url(), expected_url)

    def test_ingredient_detail_view(self):
        response = self.client.get(reverse('ingredients:ingredient-detail', kwargs={'pk': self.ingredient.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.ingredient.name)
        self.assertTemplateUsed(response, 'ingredients/detail.html')
