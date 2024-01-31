from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Recipe, RecipeIngredient, Ingredient
from django.db.models import Q


def add_product_to_recipe(request: HttpRequest):
    RecipeIngredient.objects.update_or_create(
        recipe_id=request.GET["recipe_id"],
        ingredient_id=request.GET["product_id"],
        defaults={"weight": request.GET["weight"]}
    )
    return HttpResponse(status="200")

def cook_recipe(request):
    ingredients = [x.ingredient for x in Recipe.objects.get(id=request.GET["recipe_id"]).ingredients.all()]
    print(ingredients)
    for ingredient in ingredients:
        print(ingredient)
        ingredient.counter = ingredient.counter + 1
        ingredient.save()
    return HttpResponse(status="200")

def show_recipes_without_product(request):
    ingredient = Ingredient.objects.get(pk=request.GET["product_id"])
    ingredients = RecipeIngredient.objects.filter(ingredient=ingredient, weight__gte=10)
    recipes = Recipe.objects.exclude(ingredients__in=ingredients)
    #return HttpResponse(recipes)
    return render(request, "recipes/show_recipes_without_product.html", {"ingredient": ingredient, "recipes": recipes})
