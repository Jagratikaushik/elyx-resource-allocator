import csv
import random

# Activity definitions with realistic metadata
activity_catalog = {
    "Exercise": [
        {
            "name": "Morning_Run",
            "facilitator": "Trainer",
            "location": "Gym",
            "equipment": "Treadmill",
            "metric": "Heart_Rate",
            "details": "Maintain_heart_rate_between_120_140_bpm",
            "preparation": "Dynamic_warmup_5_minutes",
            "backup": "Cycling"
        },
        {
            "name": "Yoga",
            "facilitator": "Trainer",
            "location": "Gym",
            "equipment": "Yoga_Mat",
            "metric": "Flexibility",
            "details": "Focus_on_flexibility_and_breathing",
            "preparation": "Light_stretching_before_session",
            "backup": "Home_Stretching"
        },
        {
            "name": "Cycling",
            "facilitator": "Trainer",
            "location": "Gym",
            "equipment": "Stationary_Bike",
            "metric": "Heart_Rate",
            "details": "Moderate_intensity_cardio_training",
            "preparation": "Adjust_bike_height",
            "backup": "Brisk_Walking"
        },
        {
            "name": "Strength_Training",
            "facilitator": "Trainer",
            "location": "Gym",
            "equipment": "Weights",
            "metric": "Muscle_Strength",
            "details": "Full_body_strength_workout",
            "preparation": "Warmup_and_mobility_drills",
            "backup": "Resistance_Bands"
        }
    ],

    "Food": [
        {
            "name": "Protein_Shake",
            "facilitator": "None",
            "location": "Home",
            "equipment": "None",
            "metric": "Calories",
            "details": "Consume_within_30_minutes_post_workout",
            "preparation": "Blend_protein_powder_with_milk",
            "backup": "Greek_Yogurt"
        },
        {
            "name": "Healthy_Breakfast",
            "facilitator": "None",
            "location": "Home",
            "equipment": "None",
            "metric": "Nutrition_Intake",
            "details": "High_protein_balanced_breakfast",
            "preparation": "Prepare_eggs_and_whole_grains",
            "backup": "Protein_Smoothie"
        },
        {
            "name": "Post_Workout_Meal",
            "facilitator": "None",
            "location": "Home",
            "equipment": "None",
            "metric": "Protein_Intake",
            "details": "Balanced_meal_with_protein_and_carbs",
            "preparation": "Meal_prep_before_workout",
            "backup": "Protein_Shake"
        }
    ],

    "Medication": [
        {
            "name": "Vitamin_D",
            "facilitator": "None",
            "location": "Home",
            "equipment": "None",
            "metric": "Vitamin_Level",
            "details": "Supplement_for_bone_and_immune_health",
            "preparation": "Take_after_breakfast",
            "backup": "Multivitamin"
        },
        {
            "name": "Omega3",
            "facilitator": "None",
            "location": "Home",
            "equipment": "None",
            "metric": "Omega_Level",
            "details": "Supports_cardiovascular_health",
            "preparation": "Take_with_meal",
            "backup": "Fish_Intake"
        },
        {
            "name": "Magnesium",
            "facilitator": "None",
            "location": "Home",
            "equipment": "None",
            "metric": "Mineral_Level",
            "details": "Supports_muscle_and_nerve_function",
            "preparation": "Take_before_sleep",
            "backup": "Magnesium_rich_food"
        }
    ],

    "Therapy": [
        {
            "name": "Sauna_Session",
            "facilitator": "Therapist",
            "location": "Wellness_Center",
            "equipment": "Sauna",
            "metric": "Body_Temperature",
            "details": "Heat_therapy_for_muscle_relaxation",
            "preparation": "Hydrate_before_session",
            "backup": "Hot_Bath"
        },
        {
            "name": "Ice_Bath",
            "facilitator": "Therapist",
            "location": "Wellness_Center",
            "equipment": "IceBath",
            "metric": "Recovery_Rate",
            "details": "Cold_therapy_for_inflammation_reduction",
            "preparation": "Prepare_cold_water_tub",
            "backup": "Cold_Shower"
        },
        {
            "name": "Massage_Therapy",
            "facilitator": "Therapist",
            "location": "Wellness_Center",
            "equipment": "Massage_Table",
            "metric": "Muscle_Recovery",
            "details": "Therapeutic_massage_for_muscle_recovery",
            "preparation": "Wear_comfortable_clothing",
            "backup": "Foam_Rolling"
        }
    ],

    "Consultation": [
        {
            "name": "Physio_Checkup",
            "facilitator": "Physiotherapist",
            "location": "Clinic",
            "equipment": "None",
            "metric": "Mobility_Report",
            "details": "Assess_joint_mobility_and_posture",
            "preparation": "Bring_recent_medical_reports",
            "backup": "Online_Physio_Call"
        },
        {
            "name": "Diet_Consultation",
            "facilitator": "Dietician",
            "location": "Clinic",
            "equipment": "None",
            "metric": "Diet_Report",
            "details": "Review_nutrition_and_meal_plan",
            "preparation": "Prepare_food_log_for_last_week",
            "backup": "Online_Diet_Call"
        },
        {
            "name": "Health_Coach_Call",
            "facilitator": "Coach",
            "location": "Remote",
            "equipment": "None",
            "metric": "Wellness_Score",
            "details": "Discuss_progress_and_lifestyle_habits",
            "preparation": "Review_weekly_health_metrics",
            "backup": "Email_Checkin"
        }
    ]
}

frequency_rules = {
    "Exercise": ["2/week", "3/week"],
    "Food": ["Daily"],
    "Medication": ["Daily"],
    "Therapy": ["1/week"],
    "Consultation": ["1/month"]
}

priority_rules = {
    "Exercise": ["High", "Medium"],
    "Food": ["High", "Medium"],
    "Medication": ["High"],
    "Therapy": ["Medium"],
    "Consultation": ["Medium"]
}

activity_types = list(activity_catalog.keys())

rows = []

for i in range(120):

    activity_type = random.choices(
        activity_types,
        weights=[0.30,0.25,0.20,0.15,0.10]
    )[0]

    template = random.choice(activity_catalog[activity_type])

    row = {
        "activity_id": i + 1,
        "activity_type": activity_type,
        "name": template["name"],
        "priority": random.choice(priority_rules[activity_type]),
        "frequency": random.choice(frequency_rules[activity_type]),
        "facilitator": template["facilitator"],
        "location": template["location"],
        "remote_possible": "Yes" if template["location"] in ["Home","Remote"] else "No",
        "equipment": template["equipment"],
        "details": template["details"],
        "preparation": template["preparation"],
        "backup_activity": template["backup"],
        "skip_adjustment": "Reschedule_next_available_slot",
        "metrics": template["metric"]
    }

    rows.append(row)

with open("data/activities.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Generated high-quality realistic activity dataset.")