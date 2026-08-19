"""Quick overview of the comprehension lessons in this folder."""

menu = ["masala", "iced tea", "green tea", "iced peach", "ginger tea"]
recipes = {
    "masala chai": ["ginger", "cardamom", "clove"],
    "elaichi chai": ["cardamom", "milk"],
}
tea_prices = {"masala chai": 40, "green tea": 50, "tulsi tea": 80}
daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

iced_teas = [tea for tea in menu if "iced" in tea]
unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
prices_in_usd = {tea: round(price / 80, 2) for tea, price in tea_prices.items()}
cups_sold_above_three = sum(cups for cups in (sale for sale in daily_sales) if cups > 3)

print("Iced teas:", iced_teas)
print("Unique spices:", unique_spices)
print("Prices in USD:", prices_in_usd)
print("Cups sold above 3:", cups_sold_above_three)
print("\nStudy the numbered files for focused lessons and the project.")
