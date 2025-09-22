import minecraft_data as md
import json

known_prices = json.loads(open("base_prices.json", "r").read())

def calculate_possible_prices():
    change = False
    for recipe in md.recipes:
        if not "result" in recipe or not "id" in recipe["result"]:
            continue
        
        result = recipe["result"]["id"]
        count = 1
        if "count" in recipe["result"]:
            count = recipe["result"]["count"]
        ingredients = md.get_ingredients(recipe)

        possible = True
        price = 0
        for ingredient in ingredients:
            if ingredient not in known_prices:
                possible = False
                break;
            price += known_prices[ingredient]
        
        price /= count
        if not possible:
            continue
        if result in known_prices and price >= known_prices[result]:
            continue
        known_prices[result] = price
        change = True
    return change



while calculate_possible_prices():
    pass

file = open("prices.json", "w")
file.write(json.dumps(known_prices))
