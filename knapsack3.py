def multiple_knapsacks(items, knapsack_capacities):
    items = sorted(items, key=lambda item: item[1] / item[0], reverse=True)

    num_knapsacks = len(knapsack_capacities)
    knapsacks = [[] for knapsack in range(num_knapsacks)]
    total_profits = [0] * num_knapsacks

    for item in items:
        weight, profit = item
        selected_knapsack = None
        max_profit_increase = 0

        for i in range(num_knapsacks):
            if weight <= knapsack_capacities[i]:
                profit_increase = profit
                if knapsack_capacities[i] - weight > 0:
                    profit_increase /= weight

                if profit_increase > max_profit_increase:
                    max_profit_increase = profit_increase
                    selected_knapsack = i

        if selected_knapsack is not None:
            knapsacks[selected_knapsack].append(item)
            total_profits[selected_knapsack] += profit
            knapsack_capacities[selected_knapsack] -= weight

    return knapsacks, total_profits

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

knapsack_capacities = [10, 15, 8] # Maximum knapsack capacities

knapsacks, total_profits = multiple_knapsacks(items, knapsack_capacities)

for i in range(len(knapsacks)):
    print(f"Knapsack {i + 1} - Total Profit: {total_profits[i]}")
    print("Chosen items:")
    for item in knapsacks[i]:
        print(f"  Weight: {item[0]}, Value: {item[1]}")
