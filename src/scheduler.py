import pandas as pd
import random

# Load datasets
activities = pd.read_csv("data/activities.csv")
equipment = pd.read_csv("data/equipment.csv")
specialists = pd.read_csv("data/specialists.csv")
travel = pd.read_csv("data/travel.csv")

schedule = []

time_slots = ["07:00", "09:00", "11:00", "14:00", "16:00"]

for index, activity in activities.head(30).iterrows():

    date = random.choice(travel["date"].tolist())

    # Check travel constraint
    travel_day = travel[travel["date"] == date]["travel"].values[0]

    if travel_day == "Yes" and activity["remote_possible"] == "No":
        activity_name = activity["backup_activity"]
    else:
        activity_name = activity["name"]

    schedule.append({
        "date": date,
        "time": random.choice(time_slots),
        "activity": activity_name,
        "type": activity["activity_type"],
        "location": activity["location"]
    })

# Save output
schedule_df = pd.DataFrame(schedule)

schedule_df["date"] = pd.to_datetime(schedule_df["date"])

schedule_df = schedule_df.sort_values(by=["date","time"])

schedule_df.to_csv("output/personal_plan.csv", index=False)

print("Personalized plan generated!")