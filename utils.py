import re
import random
from PyPDF2 import PdfReader
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import tempfile


# 🔹 Extract text
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


# 🔹 Clean + split text
def preprocess_text(text):
    sentences = re.split(r'\.|\n', text)
    sentences = [s.strip() for s in sentences if len(s) > 20]
    return list(set(sentences))  # remove duplicates


# 🔹 Generate questions (YOUR AI)
def generate_questions(text, two, five, ten):

    sentences = preprocess_text(text)

    questions = []

    # question templates
    def make_2_mark(s):
        return random.choice([
            f"What is {s}?",
            f"Define {s}.",
            f"Write short note on {s}.",
            f"List key points of {s}."
        ])

    def make_5_mark(s):
        return random.choice([
            f"Explain {s}.",
            f"Describe {s} in detail.",
            f"Discuss the concept of {s}.",
            f"Write about {s} with examples."
        ])

    def make_10_mark(s):
        return random.choice([
            f"Explain {s} in detail with diagram.",
            f"Discuss advantages and applications of {s}.",
            f"Write an essay on {s}.",
            f"Explain {s} with real-world examples."
        ])

    used = set()

    def get_unique_sentence():
        for s in sentences:
            if s not in used:
                used.add(s)
                return s
        return random.choice(sentences)

    # 2 marks
    for _ in range(int(two)):
        s = get_unique_sentence()
        questions.append({"question": make_2_mark(s), "marks": "2"})

    # 5 marks
    for _ in range(int(five)):
        s = get_unique_sentence()
        questions.append({"question": make_5_mark(s), "marks": "5"})

    # 10 marks
    for _ in range(int(ten)):
        s = get_unique_sentence()
        questions.append({"question": make_10_mark(s), "marks": "10"})

    return questions


# 🔹 PDF generation
def generate_pdf(questions):

    temp_file = tempfile.NamedTemporaryFile(delete=False)

    c = canvas.Canvas(temp_file.name, pagesize=A4)

    y = 800

    c.setFont("Helvetica-Bold", 16)
    c.drawString(180, y, "QUESTION PAPER")

    y -= 40
    c.setFont("Helvetica", 12)

    for i, q in enumerate(questions, 1):

        text = f"{i}. ({q['marks']} Marks) {q['question']}"

        c.drawString(50, y, text)
        y -= 25

        if y < 100:
            c.showPage()
            y = 800

    c.save()

    return temp_file.name