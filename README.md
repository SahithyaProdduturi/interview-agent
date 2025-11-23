# AI Interview Practice Agent

This project is an AI-powered interview simulator that helps users practice real interview scenarios. The agent asks follow-up questions based on user responses, adapts conversation flow, and generates a personalized feedback report at the end.

---

## Features

- Context-aware conversation using AI memory
- Custom role, difficulty level, and interviewer personality
- Dynamic follow-up questions instead of repeated prompts
- Auto-generated feedback including strengths, improvements, and scoring
- Smooth user experience with automatic input clearing
- Simple and clean UI built with Streamlit

---

## Tech Stack

| Component        | Technology              |
| ---------------- | ----------------------- |
| Frontend         | Streamlit               |
| Backend Logic    | Python                  |
| AI Model         | OpenAI API              |
| Session Handling | Streamlit Session State |

---

## Project Structure

interview_app/
┣ app.py
┣ utils.py
┣ requirements.txt
┣ README.md
┗ .gitignore

---

## How to Run

1️⃣ Clone Repository  
git clone https://github.com/YOUR_USERNAME/Interview-AI-Agent.git

cd Interview-AI-Agent

2️⃣ Create Virtual Environment  
python -m venv venv
venv\Scripts\activate (Windows)
source venv/bin/activate (Mac/Linux)

3️⃣ Install Dependencies  
pip install -r requirements.txt

4️⃣ Add Your OpenAI API Key

Open utils.py and update this line:
client = OpenAI(api_key="YOUR_API_KEY")

5️⃣ Run the Application  
streamli run app.py
