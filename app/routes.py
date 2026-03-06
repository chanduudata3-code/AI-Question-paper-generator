import os
from flask import Blueprint, render_template, request, current_app, send_file
from .services import generate_questions, generate_pdf

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/generate", methods=["POST"])
def generate():

    topic = request.form["topic"]

    two = request.form["two"]
    five = request.form["five"]
    ten = request.form["ten"]

    questions = generate_questions(topic, two, five, ten)

    pdf_path = os.path.join(
        current_app.config["GENERATED_FOLDER"],
        "question_paper.pdf"
    )

    generate_pdf(questions, pdf_path)

    return render_template("result.html", questions=questions)


@main.route("/download")
def download():

    pdf_path = os.path.join(
        current_app.config["GENERATED_FOLDER"],
        "question_paper.pdf"
    )

    return send_file(pdf_path, as_attachment=True)