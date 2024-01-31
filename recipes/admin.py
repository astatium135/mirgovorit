from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient


admin.site.register(Ingredient)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    fk_name = 'recipe'


class RecipeAdmin(admin.ModelAdmin):
    inlines = (
        RecipeIngredientInline,
    )


admin.site.register(Recipe, RecipeAdmin)