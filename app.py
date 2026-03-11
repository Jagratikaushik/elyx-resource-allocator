import streamlit as st
import pandas as pd

st.title("Elyx Resource Allocator")

st.write("Personalized Health Activity Plan")

# Load schedule
df = pd.read_csv("output/personal_plan.csv")

st.dataframe(df)

st.write("Calendar View")

for date in sorted(df["date"].unique()):
    st.subheader(date)
    day_plan = df[df["date"] == date]

    for _, row in day_plan.iterrows():
        st.write(f"{row['time']} — {row['activity']} ({row['type']})")