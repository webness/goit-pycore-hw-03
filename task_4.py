import datetime
import random

def get_upcoming_birthdays(user_list):
    current_date = datetime.date.today()
    upcoming_birthdays = []

    for user in user_list:
        birth_date = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = datetime.date(current_date.year, birth_date.month, birth_date.day)
        if current_date <= birthday_this_year <= (current_date + datetime.timedelta(days=6)):
            congratulation_date = birthday_this_year
            if birthday_this_year.weekday() in (5, 6):
                congratulation_date = birthday_this_year + \
                    datetime.timedelta(days=7 - birthday_this_year.weekday())

            upcoming_birthdays.append(
                {
                    'name': user["name"],
                    'congratulation_date': congratulation_date.strftime("%Y.%m.%d"),
                }
            )

    return upcoming_birthdays

user_data = [
    {"name": "Alice Johnson", "birthday": "1990.05.21"},
    {"name": "Bob Brown", "birthday": "1983.12.11"},
    {"name": "Charlie Davis", "birthday": "1995.07.30"},
    {"name": "Diana Evans", "birthday": "1978.11.03"},
    {"name": "Eve Foster", "birthday": "1988.09.19"},
    {"name": "Frank Green", "birthday": "2001.03.14"},
    {"name": "Grace Harris", "birthday": "1992.02.22"},
]

random.shuffle(user_data)

birthdays_to_celebrate = get_upcoming_birthdays(user_data)
print("Greetings for this week:", birthdays_to_celebrate)
