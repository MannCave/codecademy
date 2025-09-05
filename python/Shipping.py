# Standard Shipping costs
weight = 6.4
if weight <= 2:
  print("Standard Shipping Cost $", weight * 1.5 + 20)
elif weight <= 6:
  print("Standard Shipping Cost $", weight * 3.00 + 20)
elif weight <= 10:
  print("Standard Shipping Cost $", weight * 4.00 + 20)
else:
  print("Standard Shipping Cost $", weight * 4.75 + 20)
# Premium Shipping Costs
cost_ground_premium = 125.00
print("Premium Ground Shipping $", cost_ground_premium)

# Drone Shipping Costs
if weight <= 2:
  print("Drone Shipping Cost $", weight * 4.50)
elif weight <= 6:
  print("Drone Shipping Cost $", weight * 9.00)
elif weight <= 10:
  print("Drone Shipping Cost $", weight * 12.00)
else:
  print("Drone Shipping Cost $", weight * 14.25)

ground = weight * 4.00 + 20  # example for 6 < weight <= 10
premium = 125.00
drone = weight * 12.00  # example for 6 < weight <= 10
cheapest = min(ground, premium, drone)
if cheapest == ground:
    print("Cheapest method: Standard Shipping $", ground)
elif cheapest == premium:
    print("Cheapest method: Premium Ground Shipping $", premium)
else:
    print("Cheapest method: Drone Shipping $", drone)
