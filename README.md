# Titanic Dataset Chat Agent

A friendly chatbot that analyzes the famous Titanic dataset using natural language queries.
Users can ask questions in plain English and receive text-based answers as well as visual insights about the passengers.

---

## Project Objective

The goal of this project is to build an interactive chatbot that:

* Understands natural language questions
* Analyzes the Titanic passenger dataset
* Provides accurate textual answers
* Generates meaningful visualizations
* Presents everything in a clean Streamlit interface

This project was built as part of the 
Titanic Dataset Chat Agent Assignment.

---

## Tech Stack
* Python – Core programming language
* Streamlit – Frontend framework for interactive UI
* Pandas – Data analysis and processing
* Matplotlib & Seaborn – Data visualization

---

## Note on Backend & Agent Framework 
FastAPI and LangChain were explored during development for backend and agent-based reasoning.
For deployment reliability on Streamlit Cloud, the final version embeds the analysis logic directly within the Streamlit application while preserving natural language query handling and visualization behavior.

---

## Supported Questions
The chatbot currently supports questions such as:
* What percentage of passengers were male on the Titanic?
* Show me a histogram of passenger ages
* What was the average ticket fare?
* How many passengers embarked from each port?

If an unsupported question is asked, the chatbot provides guidance on what types of questions it can answer.

---

## Features
* Natural language question input
* Accurate dataset-driven responses
* Dynamic visualizations (histograms & bar charts)
* Clean and simple UI
* Fully deployed and accessible via Streamlit Cloud

---

## Live Demo
Streamlit App URL:

https://titanic-chatbot-97kwcpqurxeuifytcpwnax.streamlit.app/


---

## Project Structure
```
titanic-chatbot/
    ├── README.md             # Project documentation
    ├── app.py                # Streamlit application
    ├── requirements.txt      # Project dependencies
    ├── titanic.csv           # Titanic dataset
    └── backend/
        ├── agent.py
        ├── data.py
        └── main.py
```

---

## How to Run Locally

1. Clone the repository:
```
git clone https://github.com/your-username/titanic-chatbot.git
cd titanic-chatbot
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the Streamlit app:
```
streamlit run app.py
```

---

## Learnings & Takeaways
* Designing natural language-driven data applications
* Handling real-world deployment constraints
* Balancing architectural purity with reliability
* Building AI-focused tools with user experience in mind

---

## Future Improvements
* Reintroduce FastAPI as a backend service
* Integrate LangChain for advanced agent reasoning
* Add more analytical queries (survival rate, class-wise analysis)
* Improve NLP intent detection

---

## Author

***Rashi Gupta***

Backend & AI-focused Developer

