import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import tempfile


def generate_questions(topic, two, five, ten):

    two_templates = [
        f"Define {topic}.",
        f"List two advantages of {topic}.",
        f"Write short notes on {topic}.",
        f"State the purpose of {topic}.",
        f"What is meant by {topic}?"
    ]

    five_templates = [
        f"Explain the concept of {topic}.",
        f"Describe the features of {topic}.",
        f"Discuss the working of {topic}.",
        f"Explain the structure of {topic}.",
        f"Illustrate the applications of {topic}."
    ]

    ten_templates = [
        f"Explain {topic} in detail with examples.",
        f"Discuss advantages and limitations of {topic}.",
        f"Explain the architecture of {topic}.",
        f"Describe real-world applications of {topic}.",
        f"Explain {topic} with a detailed diagram."
    ]

    questions = []

    questions += [{"question": q, "marks": "2"} for q in random.sample(two_templates, min(two, len(two_templates)))]
    questions += [{"question": q, "marks": "5"} for q in random.sample(five_templates, min(five, len(five_templates)))]
    questions += [{"question": q, "marks": "10"} for q in random.sample(ten_templates, min(ten, len(ten_templates)))]

    return questions


def generate_pdf(questions):

    temp_file = tempfile.NamedTemporaryFile(delete=False)

    c = canvas.Canvas(temp_file.name, pagesize=A4)

    y = 800

    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, y, "QUESTION PAPER")

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