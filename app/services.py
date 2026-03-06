import random
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_questions(topic, two, five, ten):

    questions = []

    two_mark_templates = [
        f"Define {topic}.",
        f"What is {topic}?",
        f"List two advantages of {topic}.",
        f"State the purpose of {topic}.",
        f"Write short notes on {topic}."
    ]

    five_mark_templates = [
        f"Explain the concept of {topic}.",
        f"Discuss the working of {topic}.",
        f"Explain the architecture of {topic}.",
        f"Describe the features of {topic}.",
        f"Explain the advantages and limitations of {topic}."
    ]

    ten_mark_templates = [
        f"Discuss {topic} in detail with suitable examples.",
        f"Explain the complete working mechanism of {topic}.",
        f"Describe the architecture and applications of {topic}.",
        f"Discuss advantages, limitations and real-world use cases of {topic}.",
        f"Explain {topic} with a detailed diagram."
    ]

    for i in range(int(two)):
        questions.append({
            "question": random.choice(two_mark_templates),
            "marks": "2"
        })

    for i in range(int(five)):
        questions.append({
            "question": random.choice(five_mark_templates),
            "marks": "5"
        })

    for i in range(int(ten)):
        questions.append({
            "question": random.choice(ten_mark_templates),
            "marks": "10"
        })

    return questions


def generate_pdf(questions, filepath):

    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("AI Generated Question Paper", styles["Title"]))

    elements.append(Paragraph("<br/><b>Section A – 2 Marks</b>", styles["Heading2"]))

    for q in questions:
        if q["marks"] == "2":
            elements.append(Paragraph(q["question"], styles["Normal"]))

    elements.append(Paragraph("<br/><b>Section B – 5 Marks</b>", styles["Heading2"]))

    for q in questions:
        if q["marks"] == "5":
            elements.append(Paragraph(q["question"], styles["Normal"]))

    elements.append(Paragraph("<br/><b>Section C – 10 Marks</b>", styles["Heading2"]))

    for q in questions:
        if q["marks"] == "10":
            elements.append(Paragraph(q["question"], styles["Normal"]))

    pdf = SimpleDocTemplate(filepath)

    pdf.build(elements)