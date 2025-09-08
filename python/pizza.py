# Your code below:
# List of all Pizza Slices
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
# Prices of each slice of Pizza
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
# Verify Code above ^
#print(num_two_dollar_slices) 
num_pizzas = len(toppings)
# Verify Code above ^
#print(num_pizzas)
print(f"We sell", num_pizzas, "different kinds of pizza!!")

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
pizza_and_prices = sorted(pizza_and_prices)
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
pizza_and_prices.pop()
print(pizza_and_prices)
pizza_and_prices.insert(4, [2.5, "peppers"])
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
