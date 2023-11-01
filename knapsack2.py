def problem_0_1_knapsack(items, knapsack_capacity):
  length = len(items)
  table = [[0] * (knapsack_capacity + 1) for cell in range(length + 1)]
  
  for i in range(1, length + 1):
    weight, value = items[i - 1]
    for w in range(1, knapsack_capacity + 1):
      if weight > w:
        table[i][w] = table[i - 1][w]
      else:
        table[i][w] = max(table[i - 1][w], table[i - 1][w - weight] + value)

    knapsack_chosen_items = []
    chosen_items_weight = knapsack_capacity
    for i in range(length, 0, -1):
      if table[i][w] != table[i - 1][w]:
         knapsack_chosen_items.append(items[i - 1])
         chosen_items_weight -= items[i - 1][0]

  return knapsack_chosen_items, table[length][knapsack_capacity]
  
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