## MinecraftItemPriceCalculator
I wrote this to calculate sell-only prices for every item on my Minecraft server. If you only need the final prices, copy `prices.json`.

These prices are meant for selling only. Many items are intentionally priced lower than their raw cost so late-game farms don’t break the server economy.

## How it works
Prices start from manually set values for all uncraftable items (see `base_prices.json`). Craftable item prices are derived by finding the cheapest way to produce them (including smelting when it’s cheaper).

The pricing uses an end-game farming benchmark: one hour of efficient farming is valued at 100,000$. I measured how many of an item can be gathered in a set time with high-end gear, extrapolated to an hour, and scaled so that the measured quantity equals 100,000$.

Example:
To price dirt I mined as much as I could in one minute with an Efficiency V netherite shovel (≈10 stacks), extrapolated to one hour (≈600 stacks → 38,400 dirt). Scaling 38,400 to 100,000$ gives ~2.6$ per dirt.

## Run it yourself
1. Add the Minecraft data folder to `./minecraft`. Extract it from the server JAR available at https://www.minecraft.net/en-us/download/server. The data is at:
   `server.jar/META-INF/versions/1.x.x/server-1.x.x.jar/data`
   (You may need to rename the `.jar` to `.zip` or unzip it to access the files.)
2. Calculate prices from `base_prices.json`:
   ```
   python3 calculate.py
   ```
   The result will be stored in `base_prices.json`.
3. List items with no crafting recipe:
   ```
   python3 minecraft_data.py uncraftable
   ```
   This can miss items that convert back and forth (e.g., wheat <-> hay bale). `calculate.py` will warn if any items are missing.
