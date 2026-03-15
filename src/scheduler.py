import pandas as pd
import random

activities = pd.read_csv("data/activities.csv")
equipment = pd.read_csv("data/equipment.csv")
specialists = pd.read_csv("data/specialists.csv")
travel = pd.read_csv("data/travel.csv")

schedule = []

time_slots = ["07:00","09:00","11:00","14:00","16:00"]

activity_time_rules = {
    "Morning_Run": ["07:00"],
    "Yoga": ["07:00","09:00"],
    "Cycling": ["07:00","09:00"],
    "Strength_Training": ["09:00"],
    "Healthy_Breakfast": ["07:00"],
    "Protein_Shake": ["11:00"],
    "Post_Workout_Meal": ["11:00"],
    "Vitamin_D": ["07:00"],
    "Omega3": ["07:00"],
    "Magnesium": ["21:00"],
    "Diet_Consultation": ["14:00"],
    "Physio_Checkup": ["14:00"],
    "Health_Coach_Call": ["14:00"],
    "Sauna_Session": ["16:00"],
    "Ice_Bath": ["16:00"],
    "Massage_Therapy": ["16:00"]
}

# Track used time slots per day
used_slots = {}

for index, activity in activities.head(30).iterrows():

    date = random.choice(travel["date"].tolist())

    if date not in used_slots:
        used_slots[date] = []

    activity_name = activity["name"]

    # ---------- Travel constraint ----------
    travel_day = travel[travel["date"] == date]["travel"].values[0]

    if travel_day == "Yes" and activity["remote_possible"] == "No":
        activity_name = activity["backup_activity"]

    # ---------- Equipment constraint ----------
    equipment_needed = activity["equipment"]

    if equipment_needed != "None":

        eq_check = equipment[
            (equipment["equipment"] == equipment_needed) &
            (equipment["date"] == date)
        ]

        if not eq_check.empty and eq_check.iloc[0]["available"] == "No":
            activity_name = activity["backup_activity"]

    # ---------- Determine allowed time slots ----------
    allowed_times = activity_time_rules.get(activity_name, time_slots)

    # Remove already used slots
    available_slots = [t for t in allowed_times if t not in used_slots[date]]

    if not available_slots:
        continue

    time = random.choice(available_slots)

    # ---------- Specialist constraint ----------
    facilitator = activity["facilitator"]

    if facilitator != "None":

        spec_check = specialists[
            (specialists["specialist"] == facilitator) &
            (specialists["date"] == date) &
            (specialists["time_slot"] == time)
        ]

        if not spec_check.empty and spec_check.iloc[0]["available"] == "No":
            activity_name = activity["backup_activity"]

    schedule.append({
        "date": date,
        "time": time,
        "activity": activity_name,
        "type": activity["activity_type"],
        "location": activity["location"]
    })

    used_slots[date].append(time)

schedule_df = pd.DataFrame(schedule)

schedule_df["date"] = pd.to_datetime(schedule_df["date"])
schedule_df = schedule_df.sort_values(by=["date","time"])

schedule_df.to_csv("output/personal_plan.csv", index=False)

print("Personalized plan generated!")