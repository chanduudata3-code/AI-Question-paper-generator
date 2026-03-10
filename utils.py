import random

def generate_questions(topic, two, five, ten):

    two_mark_templates = [
        f"Define {topic}.",
        f"List two advantages of {topic}.",
        f"Write short notes on {topic}.",
        f"State the purpose of {topic}.",
        f"What is meant by {topic}?",
        f"Give two applications of {topic}.",
        f"List two features of {topic}."
    ]

    five_mark_templates = [
        f"Explain the concept of {topic}.",
        f"Describe the features of {topic}.",
        f"Discuss the working of {topic}.",
        f"Explain the structure of {topic}.",
        f"Illustrate the applications of {topic}.",
        f"Explain the advantages of {topic}.",
        f"Describe the components of {topic}."
    ]

    ten_mark_templates = [
        f"Explain {topic} in detail with examples.",
        f"Discuss advantages and limitations of {topic}.",
        f"Explain the architecture of {topic}.",
        f"Describe the real-world applications of {topic}.",
        f"Explain {topic} with a detailed diagram.",
        f"Discuss the working principles of {topic}.",
        f"Explain the importance of {topic} in modern systems."
    ]

    questions = []

    two_questions = random.sample(two_mark_templates, min(two, len(two_mark_templates)))
    five_questions = random.sample(five_mark_templates, min(five, len(five_mark_templates)))
    ten_questions = random.sample(ten_mark_templates, min(ten, len(ten_mark_templates)))

    for q in two_questions:
        questions.append({"question": q, "marks": "2"})

    for q in five_questions:
        questions.append({"question": q, "marks": "5"})

    for q in ten_questions:
        questions.append({"question": q, "marks": "10"})

    return questions