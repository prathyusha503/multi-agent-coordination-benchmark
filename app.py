import json
import pandas as pd
import streamlit as st

st.title("Multi-Agent Benchmark Dashboard")

with open("results.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

st.dataframe(df[["task_id", "title", "provider", "final_answer"]])

task = st.selectbox("Choose Task", df["task_id"])

row = df[df["task_id"] == task].iloc[0]

st.subheader("Transcript")

for msg in row["messages"]:
    st.write(msg)