import os
from flask import Blueprint, render_template, request, current_app, send_file
from .services import (
    extract_text_from_pdf,
    generate_questions_with_ollama,
    generate_pdf
)

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")


@main.route("/upload", methods=["POST"])
def upload_pdf():
    print("UPLOAD ROUTE HIT")

    file = request.files["file"]
    file_path = os.path.join(current_app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    text = extract_text_from_pdf(file_path)
    questions = generate_questions_with_ollama(text[:1500])

    pdf_path = os.path.join(current_app.config["GENERATED_FOLDER"], "question_paper.pdf")
    generate_pdf(questions, pdf_path)

    return render_template("result.html", questions=questions)


@main.route("/generate-topic", methods=["POST"])
def generate_from_topic():

    topic = request.form["topic"]

    easy_count = request.form.get("easy", 0)
    medium_count = request.form.get("medium", 0)
    hard_count = request.form.get("hard", 0)

    prompt = f"""
You are an exam paper generator.

Generate:
- {easy_count} Easy questions
- {medium_count} Medium questions
- {hard_count} Hard questions

Topic: {topic}

Return ONLY valid JSON in this format:
[
  {{"question": "...", "difficulty": "easy"}},
  {{"question": "...", "difficulty": "medium"}},
  {{"question": "...", "difficulty": "hard"}}
]
"""

    questions = generate_questions_with_ollama(prompt)

    pdf_path = os.path.join(current_app.config["GENERATED_FOLDER"], "question_paper.pdf")
    generate_pdf(questions, pdf_path)

    return render_template("result.html", questions=questions)


@main.route("/download")
def download():
    pdf_path = os.path.join(current_app.config["GENERATED_FOLDER"], "question_paper.pdf")
    return send_file(pdf_path, as_attachment=True)