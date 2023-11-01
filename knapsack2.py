def problem_0_1_knapsack(items, knapsack_capacity):
  ratio_of_item = [(item[1] / item[0], item) for item in items]
  ratio_of_item.sort(reverse=True)
  value_in_knapsack = 0
  capacity_left = knapsack_capacity
  knapsack = []
  
  for ratio, item in ratio_of_item:
    if capacity_left >= item[0]:
      knapsack.append(item)
      value_in_knapsack += item[1]
      capacity_left -= item[0]
    
  return knapsack, value_in_knapsack
  
items = [
[2, 40], # Item 1: weight = 2, value = 40 
[5, 30], # Item 2: weight = 5, value = 30
[10, 50], # Item 3: weight = 10, value = 50
[5, 10], # Item 4: weight = 5, value = 10
[7, 70], # Item 5: weight = 7, value = 70
[3, 15], # Item 6: weight = 3, value = 15
[2, 60], # Item 7: weight = 2, value = 60
[4, 80], # Item 8: weight = 4, value = 80
[9, 20], # Item 9: weight = 9, value = 20
[6, 50] # Item 10: weight = 6, value = 50
]

knapsack_capacity = 15 # Maximum knapsack capacity
our_knapsack, knapsack_value = problem_0_1_knapsack(items, knapsack_capacity)
print("Knapsack chosen items:")
for item in our_knapsack:
  print(f"Weight: {item[0]}, Value: {item[1]}")

print("The total knapsack value is:", knapsack_value)
