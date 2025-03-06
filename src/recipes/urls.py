from django.urls import path
from .views import home
from .views import RecipeListView, RecipeDetailView, ingredient_search

app_name = 'recipes'

urlpatterns = [
    path('', home),
    path('list/', RecipeListView.as_view(), name='recipe_list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path("ingredient-search/", ingredient_search, name="ingredient_search"),
]
