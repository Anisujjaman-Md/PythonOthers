fruit = ["apple", "banana", "orange"]
price = [1.2, 2.3, 3.4]
quantity = [10, 20, 30]

print(list(zip(fruit, price, quantity)))

for fruit, price, quantity in zip(fruit, price, quantity):
    print(f"You brought: {fruit}, Price is: {price}, {quantity} Kg")