import json
from datetime import datetime

with open("data.json", "r") as json_file:
    data = json.load(json_file)

def calculate_days_since(year, month, day):
    reference_date = datetime(2023, 12, 31) 
    current_date = datetime(year, month, day)
    delta = current_date - reference_date
    return delta.days

year = int(input("Enter the year of the reading (e.g., 2024): "))
month = int(input("Enter the month of the reading (1-12): "))
day = int(input("Enter the day of the reading (1-31): "))

gas_reading = int(input("Enter the gas meter reading: "))
electricity_reading = int(input("Enter the electricity meter reading: "))

days_since_dec31 = calculate_days_since(year, month, day)

month_names = [
    "jan", "feb", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december"
]
key_name = f"{month_names[month - 1]}_{day}"

data[key_name] = {
    "gas": gas_reading,
    "electricity": electricity_reading,
    "day": days_since_dec31
}

with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print(f"New entry added under key '{key_name}':")
print(json.dumps(data[key_name], indent=4))
