from fastapi import FastAPI
import pandas as pd

app = FastAPI()
df = pd.read_csv("titanic.csv")


@app.get("/ask")
def ask(question: str):
    q = question.lower()

    if "percentage" in q and "male" in q:
        pct = (df["Sex"] == "male").mean() * 100
        return {"type": "text", "answer": f"{pct:.2f}% of passengers were male"}

    if "average" in q and "fare" in q:
        return {
            "type": "text",
            "answer": f"Average ticket fare was {df['Fare'].mean():.2f}"
        }

    if "embarked" in q:
        return {
            "type": "data",
            "answer": df["Embarked"].value_counts().to_dict()
        }

    if "histogram" in q and "age" in q:
        return {"type": "chart", "answer": "age_histogram"}

    return {"type": "text", "answer": "Try asking about age, fare, gender, or embarkation."}