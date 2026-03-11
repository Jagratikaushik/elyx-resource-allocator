import csv
import random
from datetime import datetime, timedelta

start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 3, 31)

dates = []
current = start_date

while current <= end_date:
    dates.append(current.strftime("%Y-%m-%d"))
    current += timedelta(days=1)

equipment_list = ["Treadmill", "Sauna", "IceBath", "Yoga_Mat"]
specialists = ["Trainer", "Dietician", "Therapist"]
allied_health = ["Physiotherapist", "Dietitian", "Occupational_Therapist"]

time_slots = ["08:00-09:00", "10:00-11:00", "14:00-15:00", "16:00-17:00"]

# Equipment availability
with open("data/equipment.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["equipment", "date", "available"])

    for date in dates:
        for eq in equipment_list:
            writer.writerow([eq, date, random.choice(["Yes", "No"])])

# Specialist availability
with open("data/specialists.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["specialist", "date", "time_slot", "available"])

    for date in dates:
        for sp in specialists:
            writer.writerow([sp, date, random.choice(time_slots), random.choice(["Yes", "No"])])

# Allied health availability
with open("data/allied_health.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["role", "date", "time_slot"])

    for date in dates:
        for role in allied_health:
            writer.writerow([role, date, random.choice(time_slots)])

# Travel plans
with open("data/travel.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["date", "travel"])

    for date in dates:
        writer.writerow([date, random.choice(["Yes", "No"])])

print("Availability data generated successfully!")