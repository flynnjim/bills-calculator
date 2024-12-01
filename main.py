import json

GAS_KWH_CONV_M3 = 11.2
KWH_ELEC = 0.2377
ELEC_DAY = 0.5394
KWH_GAS = 0.0590
GAS_DAY = 0.2904


with open("data.json", "r") as json_file:
    data = json.load(json_file)


def calculate_cost(start, end):
    gas = (data[end]["gas"] - data[start]["gas"]) * GAS_KWH_CONV_M3
    elec = data[end]["electricity"] - data[start]["electricity"]
    days = data[end]["day"] - data[start]["day"]
    electricity_total = (elec * KWH_ELEC) + (days * ELEC_DAY)
    gas_total = (gas * KWH_GAS) + (days * GAS_DAY)
    cost_total = (gas * KWH_GAS) + (elec * KWH_ELEC) + (days * GAS_DAY) + (days * ELEC_DAY)
    print(f"The total cost from {start} to {end}, ({days} days) is: £{round(cost_total, 2)}")
    print(f"The cost per day {start}  to {end}, ({days} days) is: £{round(cost_total / days, 2)}")
    print(f"Electricity cost per day from {start}  to {end}, ({days} days) is: £{round(electricity_total / days, 2)}")
    print(f"Gas cost per day from {start}  to {end}, ({days} days) is: £{round(gas_total / days, 2)}")
    print(f"The cost per month at this price is: £{round(cost_total * 365 / (days * 12), 2)}")
    print(f"The cost per year at this price is: £{round(cost_total * 365 / days, 2)}\n")


months = list(data.keys())  
for i in range(len(months) - 1):
    calculate_cost(months[i], months[i + 1])
