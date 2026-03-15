import csv
import random
from datetime import datetime, timedelta

start = datetime(2026, 1, 1)
end = datetime(2026, 3, 31)

equipment_list = ["Treadmill", "Yoga_Mat", "Sauna", "IceBath", "Weights"]

specialist_schedule = {
    "Trainer": ["07:00", "09:00"],
    "Physiotherapist": ["11:00"],
    "Dietician": ["14:00"],
    "Therapist": ["16:00"]
}

dates = []

current = start
while current <= end:
    dates.append(current)
    current += timedelta(days=1)

# -------- Equipment Availability --------
with open("data/equipment.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["equipment","date","available"])

    for d in dates:
        for e in equipment_list:

            # equipment mostly available (90%)
            available = "Yes" if random.random() > 0.1 else "No"

            writer.writerow([
                e,
                d.strftime("%Y-%m-%d"),
                available
            ])


# -------- Specialist Availability --------
with open("data/specialists.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["specialist","date","time_slot","available"])

    for d in dates:

        # skip weekends
        if d.weekday() >= 5:
            continue

        for specialist, slots in specialist_schedule.items():

            for slot in slots:

                available = "Yes" if random.random() > 0.15 else "No"

                writer.writerow([
                    specialist,
                    d.strftime("%Y-%m-%d"),
                    slot,
                    available
                ])


# -------- Travel Plans --------
travel_days = set()

# generate 2 travel blocks
for _ in range(2):

    start_day = random.choice(dates)

    length = random.randint(3,6)

    for i in range(length):
        travel_days.add((start_day + timedelta(days=i)).strftime("%Y-%m-%d"))


with open("data/travel.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["date","travel"])

    for d in dates:

        date_str = d.strftime("%Y-%m-%d")

        travel = "Yes" if date_str in travel_days else "No"

        writer.writerow([date_str, travel])


print("Generated realistic availability schedules")