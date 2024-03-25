def knapsack(items, capacity):
    # Calculate the value per unit weight for each item
    for item in items:
        item['value_per_weight'] = item['value'] / item['weight']

    # Sort the items by value per unit weight in descending order
    items.sort(key=lambda x: x['value_per_weight'], reverse=True)

    total_value = 0
    knapsack_items = []

    for item in items:
        if capacity >= item['weight']:
            # Take the whole item
            knapsack_items.append(item)
            total_value += item['value']
            capacity -= item['weight']
        else:
            # Take a fraction of the item to fill the remaining capacity
            fraction = capacity / item['weight']
            knapsack_items.append({'weight': item['weight'] * fraction, 'value': item['value'] * fraction})
            total_value += item['value'] * fraction
            capacity = 0
            break

    return total_value, knapsack_items

# Test the program
items = [{'weight': 10, 'value': 60}, {'weight': 20, 'value': 100}, {'weight': 30, 'value': 120}]
capacity = 50

total_value, knapsack_items = knapsack(items, capacity)
print("Total value obtained:", total_value)
print("Items selected for the knapsack:")
for item in knapsack_items:
    print("Weight:", item['weight'], "Value:", item['value'])
