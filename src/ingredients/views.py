from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists and details
from .models import Ingredient               #to access Ingredient model

from recipesingredients.models import RecipeIngredient

# Create your views here.
class IngredientListView(ListView):           #class-based view
   model = Ingredient                         #specify model
   template_name = 'ingredients/list.html'    #specify template 

class IngredientDetailView(DetailView):  # class-based view
    model = Ingredient  # specify model
    template_name = 'ingredients/detail.html'  # specify template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes"] = RecipeIngredient.objects.filter(
            ingredient=self.object)
        return context