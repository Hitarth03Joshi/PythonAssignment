# 5. Inventory Matching and Pricing
# You have an inventory of products, each with a specific quantity and unit price. Customers place
# orders with a budget. Write a Python program to:
# • Determine if an order can be completely fulfilled within a customer's budget.
# • Prioritize items based on available quantities and prices.
# • Clearly state if the order is fulfillable, partially fulfillable, or impossible.

def fulfill_order(inventory, order, budget):
    total_cost = 0
    fulfillment = {}
    unfulfilled = {}

    # Prioritize items by (price, available quantity descending)
    sorted_items = sorted(order.items(), key=lambda x: (inventory.get(x[0], {}).get('price', float('inf')), -inventory.get(x[0], {}).get('quantity', 0)))

    for item, requested_qty in sorted_items:
        if item not in inventory:
            unfulfilled[item] = requested_qty
            continue

        price = inventory[item]['price']
        available = inventory[item]['quantity']

        qty_to_buy = min(available, requested_qty)
        cost = qty_to_buy * price

        if total_cost + cost <= budget:
            total_cost += cost
            fulfillment[item] = qty_to_buy
        else:
            # Try partial if money left
            remaining_budget = budget - total_cost
            max_affordable_qty = int(remaining_budget // price)
            if max_affordable_qty > 0:
                fulfillment[item] = max_affordable_qty
                total_cost += max_affordable_qty * price
                if requested_qty - max_affordable_qty > 0:
                    unfulfilled[item] = requested_qty - max_affordable_qty
            else:
                unfulfilled[item] = requested_qty

    if not unfulfilled:
        status = "Order is fully fulfillable."
    elif fulfillment:
        status = "Order is partially fulfillable."
    else:
        status = "Order is impossible to fulfill within budget."

    return {
        "status": status,
        "fulfilled": fulfillment,
        "unfulfilled": unfulfilled,
        "total_cost": total_cost
    }

# Example inventory and order
inventory = {
    'apple': {'price': 2, 'quantity': 10},
    'banana': {'price': 1, 'quantity': 5},
    'orange': {'price': 3, 'quantity': 8}
}

order = {
    'apple': 5,
    'banana': 5,
    'orange': 3
}

budget = 20

result = fulfill_order(inventory, order, budget)
print("Status:", result['status'])
print("Fulfilled:", result['fulfilled'])
print("Unfulfilled:", result['unfulfilled'])
print("Total Cost:", result['total_cost'])
