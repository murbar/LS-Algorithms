#!/usr/bin/python

# for each ingredient
# integer divide ingreds on hand by ingreds needed
# return minimum value (0 if we don't have any)

# import math


def recipe_batches(recipe, ingredients):
    counts = []

    for ingredient, qty in recipe.items():
        qty_on_hand = ingredients.get(ingredient, None)

        if not qty_on_hand:
            counts.append(0)
        else:
            counts.append(qty_on_hand // qty)

    return min(counts)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
