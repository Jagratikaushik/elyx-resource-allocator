import csv
import random
from datetime import datetime, timedelta

start = datetime(2026, 1, 1)
end = datetime(2026, 3, 31)

equipment = ["Treadmill", "Yoga_Mat", "Sauna", "IceBath", "Weights"]
specialists = ["Trainer", "Therapist", "Dietician", "Physiotherapist"]

times = ["07:00","09:00","11:00","14:00","16:00"]

dates = []

current = start
while current <= end:
    dates.append(current.strftime("%Y-%m-%d"))
    current += timedelta(days=1)

# equipment availability
with open("data/equipment.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["equipment","date","available"])

    for d in dates:
        for e in equipment:
            availability = "Yes" if random.random() > 0.2 else "No"
            writer.writerow([e,d,availability])

# specialists
with open("data/specialists.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["specialist","date","time_slot","available"])

    for d in dates:
        for s in specialists:
            writer.writerow([
                s,
                d,
                random.choice(times),
                "Yes" if random.random()>0.25 else "No"
            ])

# travel
with open("data/travel.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["date","travel"])

    for d in dates:
        writer.writerow([d,"Yes" if random.random()<0.1 else "No"])

print("Generated realistic availability schedules")