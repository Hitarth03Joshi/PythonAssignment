# 7. Date Difference Calculator (Real-World Scenario)
# Write a Python program that calculates the difference between two dates provided by a user.
# Scenario Example:
# A user wants to find out how many days they've lived by inputting their birthdate and today's date.
# Your program should:
# • Take two dates as input (format: dd-mm-yyyy).
# • Output the difference in days clearly

from datetime import datetime

def calculate_days_lived(birthdate_str, today_str):
    # Parse the input strings into date objects
    birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")
    today = datetime.strptime(today_str, "%d-%m-%Y")

    # Calculate the difference
    difference = today - birthdate
    print(f"You have lived for {difference.days} days.")

# Example usage
birthdate_input = input("Enter your birthdate (dd-mm-yyyy): ")
today_input = input("Enter today's date (dd-mm-yyyy): ")

calculate_days_lived(birthdate_input, today_input)
