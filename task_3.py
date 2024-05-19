import re
import random

def normalize_phone(phone):
    pattern = r"[+\d]"
    phone = "".join(re.findall(pattern, phone))
    phone = re.sub(r"^(\+38|38)?", "+38", phone)
    return phone

raw_phone_numbers = [
    "380501234567",
    "(050)8889900",
    "067\\t123 4567",
    "+380 44 123 4567",
    "(095) 234-5678\\n",
    "     0503451234",
    "38050 111 22 11   ",
    "38050-111-22-22",
    "    +38(050)123-32-34"
]

random.shuffle(raw_phone_numbers)

normalized_phone_numbers = [normalize_phone(number) for number in raw_phone_numbers]
print("Standardized phone numbers for SMS campaign:", normalized_phone_numbers)