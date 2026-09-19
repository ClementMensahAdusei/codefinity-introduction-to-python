# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, pasta aisle"
# Slice the items string to extract
candy1 = items[0:9]
candy2 = items[10:20]
dry_goods = items[21:27]
# Slice the categories string to extract
category1 = categories[0:11]
category2 = categories[13:]
# Create price variables
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
chocolate_price = "$2.00"
pasta_price = "$5.40"
# Use print() to display item names, prices, and categories.
print("We have " + candy1 + " for " + bubblegum_price + " in the " + category1)
print("We have " + candy2 + " for " + chocolate_price + " in the " + category1)
print(("We have " + dry_goods + " for " + pasta_price + " in the " + category2).lower())

