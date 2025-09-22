import minecraft_data as md
import json

known_prices = json.loads(open("base_prices.json", "r").read())

def calculate_item_price(item):
    if item in known_prices:
        if known_prices[item] == "calculating":
            return -1
        return known_prices[item]
    known_prices[item] = "calculating"
    prices = []
    for recipe in md.recipes:
        if not "result" in recipe or not "id" in recipe["result"]:
            continue
        
        recipe_item = recipe["result"]["id"]
        if recipe_item != item:
            continue
        amount = 1
        if "count" in recipe["result"]:
            amount = recipe["result"]["count"]

        ingredients = md.get_ingredients(recipe)
        price = 0
        for ingredient in ingredients: 
            item_price = calculate_item_price(ingredient)
            if item_price == -1:
                continue
            price += item_price
        prices.append(price / amount)
    price = -1
    if len(prices) == 0:
        print("no price for: " + item)
    else:
        print(item + " has the following possible prices: " + str(prices))
        price = min(prices)
    
    known_prices[item] = price
    return price

print(calculate_item_price("minecraft:diamond_sword"))

