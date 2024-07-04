from django.urls import path
from .views import AddRecipe, Recipes, RecipesDetail, DeleteRecipe, EditRecipe

urlpatterns = [
    path("add/", AddRecipe.as_view(), name="add_recipe"),
    path("", Recipes.as_view(), name="recipes"),
    path("<int:pk>/", RecipesDetail.as_view(), name="recipe_detail"),
    path('delete/<int:pk>/', DeleteRecipe.as_view(), name='delete_recipe'),
    path('edit/<int:pk>/', EditRecipe.as_view(), name='edit_recipe'),
]
