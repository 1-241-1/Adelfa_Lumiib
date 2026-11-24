food = []

for i in range(1,6):
    foods = str(input(f"Enter Order {i}: "))
    food.append(foods)

print(food)

Add = str(input(f"Enter Order to Add: "))
food.append(Add)

print(f"Updated Order: {food}")

search = str(input("Search for an order: "))
print(f"Number of Occurrence: ")

remove_order = str(input(f"Enter Order to cancel: "))
roar = remove(remove_order)

print("===== FINAL ORDER REPORT =====")
print(f"Orders: {food}")
print(f"Total Remaining Orders: {len(food)}")