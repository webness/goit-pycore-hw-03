import datetime

def get_days_from_today(target_date):
    current_date = datetime.date.today()
    days_difference = None

    try:
        parsed_date = datetime.datetime.strptime(target_date, "%Y-%m-%d").date()
        days_difference = (current_date - parsed_date).days
    except ValueError:
        print("Error: Please provide the date in 'YYYY-MM-DD' format.")

    return days_difference

input_date = input("Please enter a date in 'YYYY-MM-DD' format: ")
days_diff = get_days_from_today(input_date)
print(f"The number of days between {input_date} and today is {days_diff}.")