num_of_items = int(input("Number of items: "))

while num_of_items < 0:
    print("Invalid number of items!")
    num_of_items = int(input("Number of items: "))

i = 0
total_price = 0

while i < num_of_items:
    price = float(input("Price of item: "))
    total_price += price
    i += 1

if total_price > 100:
    amount = total_price * 0.9

print(f"Total price for {num_of_items} items is ${amount:.2f}")
