# MinecraftItemPriceCalculator
I wrote this to calculate the price of every item for my minecraft server. If you just need the prices you can copy prices.json.

# How it works
The prices of items are calculated using manually set prices for all uncraftable items (can be found in base\_prices.json)
I calculated the prices based on how many items you could farm with end game loot in one hour. One hour of farming should be worth 100000$.

e.g:
To calculate the price of dirt, I mined as much dirt es I could with a effi V netherite shovel in one minute (10 stacks) -> in one hour (600 stacks) -> 38400 should be worth 100000$ -> one dirt is worth 2.6$

The script then goes through all craftable items and looks for the cheapest way to craft it (this includes methods like smelting without price increase).

# Run it yourself
Before you can run the script you will have to replace the minecraft folder with the actual minecraft folder.
