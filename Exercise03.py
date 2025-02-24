groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]

while True:
    print("Grocery List:")
    for i in groceries:
        print(i)
    print()
    item = str(input("What item do you want to remove from the grocery list?"))
    if (item == "stop"):
        break
    elif (item in groceries):
        groceries.remove(item)
        if len(groceries) == 0:
            print("There are no more items on the list.")
            break
    else:
        print("Invalid input. Please try again.")
        print()