from django.db import models


class Ingredient(models.Model):
    name = models.CharField(verbose_name="название", unique=True, max_length=255)
    counter = models.PositiveIntegerField(verbose_name="сколько раз", default=0, help_text="Сколько раз готовились блюда с данным ингридиентом")

    class Meta:
        verbose_name = "ингредиент"
        verbose_name_plural = "ингредиенты"

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(verbose_name="Название", unique=True, max_length=255)

    class Meta:
        verbose_name = "рецепт"
        verbose_name_plural = "рецепты"

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    ingredient = models.ForeignKey(Ingredient, verbose_name="Ингредиент", on_delete=models.CASCADE)
    weight = models.PositiveIntegerField(verbose_name="вес (в граммах)")

    class Meta:
        unique_together = (('recipe', 'ingredient'),)

    def __str__(self):
        return "%s %sгр." % (self.ingredient.name, self.weight)