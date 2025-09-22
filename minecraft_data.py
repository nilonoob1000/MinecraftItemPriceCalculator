import json
import os
import sys

recipe_folder = "minecraft/data/minecraft/recipe/"

if not os.path.isdir(recipe_folder):
    print("recipe folder not found!")
    print("Have you imported the minecraft folder as instructed in the README?")
    sys.exit("")

recipe_files = [f for f in os.listdir(recipe_folder) if os.path.isfile(recipe_folder + f)]

recipes = []
for recipe_file in recipe_files:
    recipes.append(json.loads(open(recipe_folder + recipe_file).read()))

craftable_items = []

for recipe in recipes:
    if not "result" in recipe:
        continue

    result = recipe["result"]    

    if not ("id" in result):
        continue

    item = recipe["result"]["id"]
    if item in craftable_items:
        continue
    craftable_items.append(item)
print("found " + str(len(craftable_items)) + " craftable_items")

def get_ingredients(recipe):
    ingredients = []
    
    def add_ingredient(ingredient):
        if isinstance(ingredient, str):
            ingredients.append(ingredient)
        elif "item" in ingredient:
            ingredients.append(ingredient["item"])
        elif "tag" in ingredient:
            ingredients.append("tag:" + ingredient["tag"])
        else:
            add_ingredient(ingredient[0])

    if "ingredient" in recipe:
        add_ingredient(recipe["ingredient"])
    elif "ingredients" in recipe:
        for ingredient in recipe["ingredients"]:
            add_ingredient(ingredient)
    elif "key" in recipe:
        for row in recipe["pattern"]:
            for item_key in row:
                if item_key == ' ':
                    continue
                add_ingredient(recipe["key"][item_key])
    
    return ingredients

def get_uncraftable_items():
    uncraftable_items = {}
    for recipe in recipes:
        for ingredient in get_ingredients(recipe):
            if ingredient not in uncraftable_items and ingredient not in craftable_items:
                uncraftable_items[ingredient] = 1
    return uncraftable_items

if len(sys.argv) > 1 and sys.argv[1] == 'uncraftable':
    print(json.dumps(get_uncraftable_items()))
