import os
import json
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are an expert interview assistant. Conduct the mock interview naturally.

Rules:
- Ask one question at a time.
- If the user gives unclear, short, or irrelevant responses, follow up politely.
- Adjust tone based on user persona.
- Keep responses under 200 words.
"""

def build_messages(history, role, difficulty, persona):
    metadata = f"Role: {role}. Difficulty: {difficulty}. Persona: {persona}."
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "system", "content": metadata}
    ]
    messages.extend(history[-10:])
    return messages


def call_openai_chat(role, difficulty, persona, history, model="gpt-4o-mini"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=build_messages(history, role, difficulty, persona),
            temperature=0.3,
            max_tokens=400
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"(Error calling model: {e})"


def generate_feedback(role, difficulty, history, model="gpt-4o-mini"):
    conversation = "\n".join([f"{m['role']}: {m['content']}" for m in history])

    evaluation_prompt = f"""
Evaluate the interview:

Return JSON with:
- summary
- strengths (list)
- improvements (list)
- scores (Communication/Technical/Structure 1-5)
"""

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": evaluation_prompt + conversation}],
            temperature=0.3
        )

        try:
            return json.loads(response.choices[0].message.content)
        except:
            return {"summary": response.choices[0].message.content}

    except Exception as e:
        return {"summary": f"(Error: {e})"}


def save_transcript(history, role, difficulty):
    timestamp = int(time.time())
    filename = f"transcript_{role}_{difficulty}_{timestamp}.txt".replace(" ", "_")

    with open(filename, "w", encoding="utf-8") as f:
        for msg in history:
            sender = "USER" if msg["role"] == "user" else "BOT"
            f.write(f"{sender}: {msg['content']}\n\n")

    return filename
