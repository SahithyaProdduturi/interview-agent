# Interview Practice Partner – AI Agent

This project is submitted as part of the Agentic AI Internship Assignment.

---

### 🎯 Overview

The Interview Practice Partner is an interactive conversational AI agent designed to help users practice job interviews. The agent conducts mock interviews, asks follow-up questions based on user responses, adapts to different user behaviors, and generates structured feedback at the end.

---

### 🛠️ Features

- Role-based mock interviews (Software Engineer, Sales, Retail, Data Scientist)
- Dynamic follow-up questions and adaptive conversation
- Handles multiple user personas:
  - Efficient user
  - Confused user
  - Chatty user
  - Edge-case user
- Generates structured feedback including:
  - Strengths
  - Improvements
  - Suggested actions
  - Numeric scoring (Communication, Technical, Structure)
- Saves conversation transcript locally

---

### 🧠 Architecture & Design Decisions

- Built using **Streamlit** for user interaction and **OpenAI API** for conversational intelligence.
- Uses prompt-based logic to simulate realistic interview behavior rather than scripted questioning.
- The agent uses short-term memory to maintain context while preventing excessive token usage.
- Feedback is generated in structured JSON format for consistency.

---

### 📂 Assignment Reference

The original assignment instructions provided are included in this repository:

`AI Agent Building Assignment - Eightfold.pdf`

---

### 🚀 How to Run

#### 1. Create Virtual Environment

```bash
python -m venv venv
```
