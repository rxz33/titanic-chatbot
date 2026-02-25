import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

st.set_page_config(page_title="Titanic Chatbot", page_icon="🚢")

st.title("🚢 Titanic Dataset Chatbot")
st.write("Ask questions about Titanic passengers using natural language.")

# Load dataset safely
BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / "titanic.csv")

question = st.text_input("Ask a question")

if question:
    q = question.lower()

    if "percentage" in q and "male" in q:
        pct = (df["Sex"] == "male").mean() * 100
        st.success(f"{pct:.2f}% of passengers were male")

    elif "average" in q and "fare" in q:
        st.success(f"Average ticket fare was {df['Fare'].mean():.2f}")

    elif "embarked" in q:
        st.subheader("Passengers by embarkation port")
        st.bar_chart(df["Embarked"].value_counts())

    elif "histogram" in q and "age" in q:
        st.subheader("Age distribution of passengers")
        fig, ax = plt.subplots()
        sns.histplot(df["Age"].dropna(), bins=20, ax=ax)
        st.pyplot(fig)

    else:
        st.info("Try asking about age, fare, gender, or embarkation.")