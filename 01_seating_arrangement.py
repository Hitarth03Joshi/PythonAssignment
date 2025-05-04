# 1. Seating Arrangement Problem
# You have N guests attending a dinner party. Each guest has exactly two preferred neighbors they'd
# like to sit next to. Write a Python function that:
# • Accepts the number of guests and their neighbor preferences.
# • Determines a valid circular seating arrangement satisfying all preferences.
# • If no arrangement is possible, clearly state that.


from itertools import permutations

def find_seating_arrangement(guests):
    guest_names = list(guests.keys())
    
    def is_valid(arrangement):
        n = len(arrangement)
        for i in range(n):
            left = arrangement[(i - 1) % n]
            right = arrangement[(i + 1) % n]
            person = arrangement[i]
            # Each person must have both left and right as their preferred neighbors
            if not (left in guests[person] and right in guests[person]):
                return False
        return True

    for perm in permutations(guest_names):
        if is_valid(perm):
            return list(perm)  # Valid circular arrangement found
    
    return "No valid seating arrangement possible."

# Example input
guests = {
    'Alice': ['Bob', 'Carol'],
    'Bob': ['Alice', 'David'],
    'Carol': ['Alice', 'David'],
    'David': ['Bob', 'Carol']
}

result = find_seating_arrangement(guests)
print(result)
