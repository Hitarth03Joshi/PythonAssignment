# 8. Electricity Bill Calculation (Business Logic)
# An electricity provider charges consumers based on slabs of electricity usage:
# Usage (kWh) Price per unit ( ) ₹
# 0-100 5
# 101-300 7
# 301-500 10
# Above 500 15
# Write a Python program that:
# • Accepts electricity usage (in kWh) from the user.
# • Clearly calculates and displays the bill, explaining the charges for each slab separately.
# Example Input: 450 kWh
# Example Output:
# Electricity Bill:
# 0-100 units @ 5/unit = 500 ₹ ₹
# 101-300 units @ 7/unit = 1400 ₹ ₹
# 301-450 units @ 10/unit = 1500 ₹ ₹
# Total Amount Payable = 3400 

def calculate_electricity_bill(units):
    total = 0
    print("Electricity Bill:")

    if units <= 0:
        print("No usage. No bill.")
        return

    if units > 0:
        slab_units = min(units, 100)
        slab_amount = slab_units * 5
        print(f"0-100 units @ ₹5/unit = ₹{slab_amount}")
        total += slab_amount

    if units > 100:
        slab_units = min(units - 100, 200)
        slab_amount = slab_units * 7
        print(f"101-300 units @ ₹7/unit = ₹{slab_amount}")
        total += slab_amount

    if units > 300:
        slab_units = min(units - 300, 200)
        slab_amount = slab_units * 10
        print(f"301-500 units @ ₹10/unit = ₹{slab_amount}")
        total += slab_amount

    if units > 500:
        slab_units = units - 500
        slab_amount = slab_units * 15
        print(f"Above 500 units @ ₹15/unit = ₹{slab_amount}")
        total += slab_amount

    print(f"Total Amount Payable = ₹{total}")

# Example usage
usage_input = int(input("Enter electricity usage in kWh: "))
calculate_electricity_bill(usage_input)
