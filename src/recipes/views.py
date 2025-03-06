import random
from django.shortcuts import render
# to display lists and details
from django.views.generic import ListView, DetailView
from .models import Recipe  # to access Recipe model

from recipesingredients.models import RecipeIngredient

from django.contrib.auth.mixins import LoginRequiredMixin


# Welcome page
def home(request):
    return render(request, 'recipes/recipes_home.html')



# The list of all recipes


class RecipeListView(LoginRequiredMixin, ListView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/list.html'  # specify template

# The detail of recipe


class RecipeDetailView(LoginRequiredMixin, DetailView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/detail.html'  # specify template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = RecipeIngredient.objects.filter(
            recipe=self.object)
        return context
