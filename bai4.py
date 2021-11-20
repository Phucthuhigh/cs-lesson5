n = int(input("Number of items: "))
print("")
a = []
for i in range(n):
    name_food = input(f"Item {i + 1}: ")
    price_food = float(input(f"Price of item {i + 1}: "))
    item = {
        "name": name_food,
        "price": price_food
    }
    a.append(item)
    print("")

total_price = 0
for i in range(n):
    total_price += a[i]["price"]

average_price = round(total_price / n, 2)

filter_list = []

for i in range(n):
    if a[i]["price"] > average_price:
        filter_list.append(a[i])

print("")

print(f"Average price: {average_price}")
print("Item(s) above average price: ", end="")
for i in filter_list:
    print(f"('{i['name']}, {i['price']}')", end=" ")
