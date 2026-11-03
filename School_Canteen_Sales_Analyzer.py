total_sales = 0
item = 0
target1 = 0
target2 = 0

number_of_items = int(input("Enter the number of item: "))

for i in range(1, number_of_items+1):
    item = int(input(f"Enter sales for item {i}: "))
    total_sales += item
    if item >= 500:
        target1 += 1
    else:
        target2 += 1

average_sales = 0

def calculate_average(total_sales, number_of_items):
    average_sales = total_sales / number_of_items
    return average_sales

def result(average_sales):
    print("CANTEEN SALES REPORT")
    print(f"Average sales: PHP{average_sales} | Meeting Target: {target1} | Below Target: {target2}")

average_sales = calculate_average(total_sales, number_of_items)
result(average_sales)
