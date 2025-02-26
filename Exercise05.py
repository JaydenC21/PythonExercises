menu = {"Pizza": 1.99, "Soda":  0.69, "Double Chunk Chocolate Chip Cookie": 2.49}

def add(item, price):
    menu[item] = price

add("Nothing", 999.99)
print(menu)