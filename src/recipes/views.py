from django.shortcuts import render
# to display lists and details
from django.views.generic import ListView, DetailView
from .models import Recipe  # to access Recipe model

from ingredients.models import Ingredient
from recipesingredients.models import RecipeIngredient


# Welcome page
def home(request):
    return render(request, 'recipes/recipes_home.html')

# The list of all recipes
class RecipeListView(ListView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/list.html'  # specify template

# The detail of recipe
class RecipeDetailView(DetailView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/detail.html'  # specify template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = RecipeIngredient.objects.filter(
            recipe=self.object)
        return context
