from django.urls import path
from .views import AddRecipe, Recipes, RecipesDetail

urlpatterns = [
    path("", AddRecipe.as_view(), name="add_recipe"),
    path("recipes/", Recipes.as_view(), name="recipes"),
    path("<int:pk>/", RecipesDetail.as_view(), name="recipe_detail"),
]
