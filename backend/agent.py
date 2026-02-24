import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

df = pd.read_csv("titanic.csv")

llm = ChatOpenAI(temperature=0)

prompt = PromptTemplate(
    input_variables=["question"],
    template="""
You are analyzing the Titanic dataset.

Question: {question}

Classify the intent as one of:
- percentage_male
- age_histogram
- average_fare
- embark_counts
- unknown

Return ONLY the intent name.
"""
)

def ask_agent(question: str):
    intent = llm.invoke(prompt.format(question=question)).content.lower()

    if "percentage_male" in intent:
        pct = (df["Sex"] == "male").mean() * 100
        return f"{pct:.2f}% of passengers were male."

    if "average_fare" in intent:
        return f"Average ticket fare was {df['Fare'].mean():.2f}"

    if "embark_counts" in intent:
        return df["Embarked"].value_counts().to_dict()

    return "I can answer questions about gender, age, fare, and embarkation."