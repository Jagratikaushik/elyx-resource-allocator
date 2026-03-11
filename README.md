# Elyx Resource Allocator

## Overview
This project implements a simplified version of Elyx's Resource Allocator system.  
It converts a health action plan into scheduled activities while considering resource constraints.

## Components

1. Activity Dataset Generator
Creates 100 realistic health activities.

2. Availability Generator
Creates availability schedules for:
- Equipment
- Specialists
- Allied Health Professionals
- Travel Plans

3. Scheduler
Reads activities and availability data and generates a personalized plan.

## Assumptions

- Activities are randomly scheduled within the available date range.
- If the client is traveling and the activity is not remote, a backup activity is used.
- Equipment and specialist availability are simulated randomly.
- Time slots are simplified to fixed intervals.

## Output

The system generates a file:

output/personal_plan.csv


which represents the personalized activity calendar.

## How to Run

Generate activities:

python src/generate_activities.py

Generate availability:

python src/generate_availability.py

Generate schedule:

python src/scheduler.py



## Technologies Used

- Python
- Pandas
- CSV datasets