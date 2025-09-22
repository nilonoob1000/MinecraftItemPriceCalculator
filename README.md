# MinecraftItemPriceCalculator

I wrote this to calculate the price of every item for my minecraft server. If you just need the prices you can copy prices.json.

# How it works

The prices of items are calculated using manually set prices for all uncraftable items (can be found in base_prices.json)
I calculated the prices based on how many items you could farm with end game loot in one hour. One hour of farming should be worth 100000$.

e.g:
To calculate the price of dirt, I mined as much dirt es I could with a efficiency V netherite shovel in one minute (10 stacks) -> in one hour (600 stacks) -> 38400 should be worth 100000$ -> one dirt is worth 2.6$

The script then goes through all craftable items and looks for the cheapest way to craft it (this includes methods like smelting without price increase).

# Run it yourself

Before you can run the script you will have to add the minecraft data folder into ./minecraft. you can find it in the server.jar from https://www.minecraft.net/en-us/download/server
at server.jar/META-INF/versions/1.x.x/server-1.x.x.jar/data you might need to rename the .jar files to .zip or unzip them to navigate into.

to calculate the prizes based on the base_prices you can run
`python3 calculate.py` the result will be stored in base_prices.json

you can run `python3 minecraft_data.py uncraftable` to get a list of all items with no crafting recipe. This misses items like wheat that can be crafted back and forth into a block. The calculate.py script will warn you if any items are missing.
