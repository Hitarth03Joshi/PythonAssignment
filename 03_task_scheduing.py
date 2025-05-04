# 3. Task Scheduling Problem (Optimization)
# A software engineer has multiple tasks to complete. Each task has:
# • a deadline (day by which it must be finished),
# • an amount of time it takes to complete (in days).
# Write a Python function to:
# • Determine the maximum number of tasks the engineer can complete without missing
# deadlines.
# Input Example:
# tasks = [
#  {'name': 'Task 1', 'deadline': 4, 'duration': 2},
#  {'name': 'Task 2', 'deadline': 3, 'duration': 1},
#  {'name': 'Task 3', 'deadline': 2, 'duration': 1},
#  {'name': 'Task 4', 'deadline': 1, 'duration': 2},
# ]

import heapq

def max_tasks(tasks):
    # Step 1: Sort tasks by deadline
    tasks.sort(key=lambda x: x['deadline'])

    total_time = 0
    max_heap = []  # will store (-duration, task) so we can pop longest duration

    for task in tasks:
        duration = task['duration']
        deadline = task['deadline']

        # Add the task
        total_time += duration
        heapq.heappush(max_heap, (-duration, task))

        # If we exceed deadline, remove the longest task
        if total_time > deadline:
            removed_duration, removed_task = heapq.heappop(max_heap)
            total_time += removed_duration  # subtract (negative value)
    
    # Extract selected tasks
    selected_tasks = [task['name'] for _, task in max_heap]
    return selected_tasks

# Example input
tasks = [
    {'name': 'Task 1', 'deadline': 4, 'duration': 2},
    {'name': 'Task 2', 'deadline': 3, 'duration': 1},
    {'name': 'Task 3', 'deadline': 2, 'duration': 1},
    {'name': 'Task 4', 'deadline': 1, 'duration': 2},
]

result = max_tasks(tasks)
print("Tasks that can be completed:", result)
