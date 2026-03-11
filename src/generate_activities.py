import csv
import random

activity_types = ["Exercise", "Food", "Medication", "Therapy", "Consultation"]

exercise_names = ["Morning_Run", "Evening_Yoga", "Cycling", "Strength_Training", "Swimming"]
food_names = ["Protein_Shake", "Healthy_Breakfast", "Salad_Meal", "Green_Smoothie"]
medication_names = ["Vitamin_D", "Omega3", "Multivitamin", "Calcium"]
therapy_names = ["Sauna_Session", "Ice_Bath", "Massage_Therapy"]
consultation_names = ["Diet_Consultation", "Physio_Checkup", "Health_Coach_Call"]

facilitators = ["Trainer", "Dietician", "Therapist", "Physiotherapist", "None"]
locations = ["Gym", "Home", "Clinic", "Wellness_Center"]

frequencies = ["Daily", "3/week", "2/week", "1/week", "1/month"]
priorities = ["High", "Medium", "Low"]

file_path = "data/activities.csv"

with open(file_path, mode="w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "activity_id","activity_type","name","priority","frequency",
        "facilitator","location","remote_possible","equipment",
        "details","preparation","backup_activity","skip_adjustment","metrics"
    ])

    for i in range(1,101):

        activity_type = random.choice(activity_types)

        if activity_type == "Exercise":
            name = random.choice(exercise_names)
            equipment = "Treadmill"
            metrics = "Heart_Rate"

        elif activity_type == "Food":
            name = random.choice(food_names)
            equipment = "None"
            metrics = "Calories"

        elif activity_type == "Medication":
            name = random.choice(medication_names)
            equipment = "None"
            metrics = "Vitamin_Level"

        elif activity_type == "Therapy":
            name = random.choice(therapy_names)
            equipment = "Sauna"
            metrics = "Body_Temperature"

        else:
            name = random.choice(consultation_names)
            equipment = "None"
            metrics = "Health_Report"

        writer.writerow([
            i,
            activity_type,
            name,
            random.choice(priorities),
            random.choice(frequencies),
            random.choice(facilitators),
            random.choice(locations),
            random.choice(["Yes","No"]),
            equipment,
            "Health_related_activity",
            "Basic_preparation",
            "Backup_activity",
            "Reschedule_next_day",
            metrics
        ])

print("100 activities generated successfully!")