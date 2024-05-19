import random

def get_numbers_ticket(low, high, count):
    try:
        if low > high:
            raise ValueError("The minimum number should be less than or equal to the maximum number.")
        if count > (high - low + 1):
            raise ValueError("The quantity of numbers should not exceed the range between the minimum and maximum numbers.")
        return random.sample(range(low, high + 1), count)
    except ValueError as error_message:
        print(f"Error: {error_message}")
        return []

low_number = int(input("Enter the minimum number: "))
high_number = int(input("Enter the maximum number: "))
number_count = int(input("Enter the quantity of numbers: "))
lottery_numbers = get_numbers_ticket(low_number, high_number, number_count)
print("Your lottery numbers:", lottery_numbers)