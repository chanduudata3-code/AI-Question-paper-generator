import pdfplumber
import random
import requests
import json
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


# 1️⃣ Extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + " "
    return text


# 2️⃣ Generate Questions Using Ollama
def generate_questions_with_ollama(prompt_text):

    url = "http://localhost:11434/api/generate"

    system_prompt = f"""
You are an exam paper generator.

Generate:
- 3 Easy questions
- 2 Medium questions
- 1 Hard question

Topic: {prompt_text}

Return ONLY valid JSON.
No explanation.
No text outside JSON.

Format:
[
  {{"question": "...", "difficulty": "easy"}},
  {{"question": "...", "difficulty": "medium"}},
  {{"question": "...", "difficulty": "hard"}}
]
"""

    payload = {
        "model": "llama3",
        "prompt": system_prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    result = response.json()

    raw_output = result.get("response", "").strip()

    print("RAW OLLAMA OUTPUT:", raw_output)

    try:
        questions = json.loads(raw_output)
    except Exception as e:
        print("JSON ERROR:", e)
        questions = []

    return questions


# 3️⃣ Blueprint Selection (Optional Safety Layer)
def generate_paper(questions, blueprint):
    paper = []

    for level, count in blueprint.items():
        filtered = [q for q in questions if q["difficulty"] == level]

        if len(filtered) >= count:
            selected = random.sample(filtered, count)
        else:
            selected = filtered

        paper.extend(selected)

    return paper


# 4️⃣ PDF Generator
def generate_pdf(questions, file_path):

    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("<b>AI Generated Question Paper</b>", styles["Title"]))

    for i, q in enumerate(questions):
        elements.append(Paragraph(f"{i+1}. {q['question']} ({q['difficulty']})", styles["Normal"]))

    doc.build(elements)