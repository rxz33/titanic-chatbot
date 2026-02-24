import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🚢 Titanic Dataset Chatbot")

question = st.text_input("Ask a question about the Titanic dataset")

if question:
    res = requests.get(
        "http://127.0.0.1:8000/ask",
        params={"question": question}
    )

    data = res.json()

    if data["type"] == "text":
        st.success(data["answer"])

    elif data["type"] == "data":
        st.bar_chart(data["answer"])

    elif data["type"] == "chart":
        df = pd.read_csv("titanic.csv")
        fig, ax = plt.subplots()
        sns.histplot(df["Age"].dropna(), bins=20, ax=ax)
        st.pyplot(fig)